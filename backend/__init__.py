from __future__ import absolute_import, unicode_literals
from .celery import app as backend

__all__ = ('backend',)
