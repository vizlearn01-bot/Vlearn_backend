#!/usr/bin/env bash
# ==============================================================================
# VLearn Backend — Render Free Tier Unified Startup Script
# Co-locates Celery Worker + Gunicorn WSGI within a single 512MB Web Service container
# ==============================================================================
set -e

# Tracking child process PIDs
CELERY_PID=""
GUNICORN_PID=""

# Graceful termination handler
cleanup() {
    local exit_code=$?
    trap - SIGTERM SIGINT EXIT
    echo "[SHUTDOWN] Signal received or process exited ($exit_code). Stopping services..."

    if [ -n "$CELERY_PID" ] && kill -0 "$CELERY_PID" 2>/dev/null; then
        echo "[SHUTDOWN] Sending SIGTERM to Celery worker (PID: $CELERY_PID)..."
        pkill -TERM -P "$CELERY_PID" 2>/dev/null || true
        kill -TERM "$CELERY_PID" 2>/dev/null || true
    fi

    if [ -n "$GUNICORN_PID" ] && kill -0 "$GUNICORN_PID" 2>/dev/null; then
        echo "[SHUTDOWN] Sending SIGTERM to Gunicorn (PID: $GUNICORN_PID)..."
        kill -TERM "$GUNICORN_PID" 2>/dev/null || true
    fi

    # Wait for child processes to finish cleanly
    [ -n "$GUNICORN_PID" ] && wait "$GUNICORN_PID" 2>/dev/null || true
    [ -n "$CELERY_PID" ] && wait "$CELERY_PID" 2>/dev/null || true

    echo "[SHUTDOWN] All services terminated."
    if [ "$exit_code" -eq 143 ] || [ "$exit_code" -eq 130 ]; then
        exit 0
    fi
    exit "$exit_code"
}

trap cleanup SIGTERM SIGINT EXIT

echo "[STARTUP] Running database migrations..."
python manage.py migrate --noinput

echo "[STARTUP] Checking for Celery / Redis broker configuration..."
# Check if REDIS_URL or CELERY_BROKER_URL is set in environment
if [ -n "$REDIS_URL" ] || [ -n "$CELERY_BROKER_URL" ]; then
    echo "[STARTUP] Redis broker detected. Starting lightweight Celery worker in background..."
    echo "[STARTUP] Queues monitored: heavy_ops, default, celery"

    # Run Celery worker with solo pool inside a resilient supervisor loop.
    # If the worker recycles or drops connection, it restarts automatically without taking down the web server.
    (
        while true; do
            celery -A Nexus_backend worker \
                --loglevel=info \
                --pool=solo \
                --concurrency=1 \
                -Q heavy_ops,default,celery \
                --without-gossip \
                --without-mingle \
                --without-heartbeat || true
            echo "[CELERY] Worker exited. Restarting in 5 seconds..."
            sleep 5
        done
    ) &
    CELERY_PID=$!
    echo "[STARTUP] Celery worker supervisor started with PID: $CELERY_PID"
else
    echo "[STARTUP] No REDIS_URL or CELERY_BROKER_URL provided."
    echo "[STARTUP] Background tasks will utilize in-process daemon thread fallback."
fi

echo "[STARTUP] Starting Gunicorn WSGI HTTP server on port ${PORT:-10000} (1 worker, 2 threads)..."
gunicorn Nexus_backend.wsgi:application \
    --bind 0.0.0.0:${PORT:-10000} \
    --workers 1 \
    --threads 2 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile - &
GUNICORN_PID=$!

echo "[STARTUP] Gunicorn running with PID: $GUNICORN_PID. Monitoring services..."

# Wait for Gunicorn as the primary web service.
# The web server must stay running to serve traffic even if Celery restarts or recycles.
wait "$GUNICORN_PID"
EXIT_STATUS=$?

echo "[MONITOR] Gunicorn exited with status $EXIT_STATUS. Exiting container..."
exit "$EXIT_STATUS"
