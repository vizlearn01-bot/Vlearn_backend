"""Signal management utilities for curriculum publishing.

Provides context managers to safely disable automatic bootstrap signals
(e.g., auto-creating default pedagogy templates on Subject creation)
during one-way curriculum synchronization.
"""

import logging
from contextlib import contextmanager
from django.db.models.signals import post_save

logger = logging.getLogger(__name__)


@contextmanager
def disable_curriculum_signals():
    """Temporarily disconnects auto-bootstrap signals during curriculum publishing.

    Rationale:
    When a Subject is published to production, it already has its authoring-defined
    PedagogyTemplate and GenerationRule records published in topological sequence.
    If the Subject post_save signal fired, it would generate duplicate default
    PedagogyTemplate and GenerationRule records on the default database.
    Disconnecting the signal during the publish transaction guarantees signal-safety.
    """
    from curriculum.models import Subject, create_default_pedagogy_template

    disconnected = post_save.disconnect(create_default_pedagogy_template, sender=Subject)
    if disconnected:
        logger.debug("Disconnected create_default_pedagogy_template signal for Subject.")
    try:
        yield
    finally:
        post_save.connect(create_default_pedagogy_template, sender=Subject)
        logger.debug("Reconnected create_default_pedagogy_template signal for Subject.")
