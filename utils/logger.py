import logging

# Configure the logger
debug_logger = logging.getLogger("debug")
debug_logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("debug_logs.txt")
handler.setFormatter(logging.Formatter("%(asctime)s - PRINT - %(message)s"))
debug_logger.addHandler(handler)


# Custom print function
def debug_print(*args, **kwargs):
    # Get the original print output
    import builtins
    from io import StringIO

    # Capture what would be printed
    temp_out = StringIO()
    builtins.print(*args, file=temp_out, **kwargs)
    output = temp_out.getvalue().strip()

    # Log it
    debug_logger.debug(output)

    # Also print normally
    builtins.print(*args, **kwargs)


# Usage:
# debug_print("This will be logged and printed")


def get_custom_logging_config():
    """
    Returns a custom logging configuration dictionary for Django.
    This configuration includes handlers for writing logs to files and the console.
    """
    return {
        "version": 1,  # Dictconfig format version - should always be 1
        "disable_existing_loggers": False,  # Keep existing loggers enabled
        # Define how log messages will be formatted
        "formatters": {
            # Detailed format for error logs in the file
            "verbose": {
                "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
                "style": "%",  # Using % style placeholders
            },
            # Simplified format for console output during development
            "simple": {
                "format": "%(levelname)s %(message)s",
                "style": "%",
            },
        },
        # Define where logs will be sent
        "handlers": {
            # Handler for writing errors to a file
            "error_file": {
                "level": "ERROR",  # Only capture ERROR level and above
                "class": "logging.FileHandler",  # Use built-in file handler
                "filename": "error_logs.txt",  # Log file location in project root
                "formatter": "verbose",  # Use the detailed format defined above
            },
            "warning_file": {
                "level": "WARNING",  # Capture WARNING level and above
                "class": "logging.FileHandler",
                "filename": "warning_logs.txt",  # Separate file for warnings
                "formatter": "verbose",
            },
        },
        # Configure specific loggers
        "loggers": {
            # Django's built-in logging
            "django": {
                "handlers": ["error_file", "warning_file"],
                "level": "WARNING",
                "propagate": True,  # Pass messages to parent loggers
            },
        },
        # Root logger configuration (catches all other logs not caught by specific loggers)
        "root": {
            # Same handler logic as django logger
            "handlers": ["error_file", "warning_file"],
            "level": "WARNING",
        },
    }
