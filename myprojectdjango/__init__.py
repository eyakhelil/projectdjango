from __future__ import absolute_import, unicode_literals

# Import Celery automatiquement quand Django démarre
from .celery import app as celery_app

__all__ = ('celery_app',)
