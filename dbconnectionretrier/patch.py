from contextlib import contextmanager

import aspectlib

from django.db.backends.base.base import BaseDatabaseWrapper

from .ensure_connection import ensure_connection


def patch_ensure_connection():
    """Monkey patch BaseDatabaseWrapper.ensure_connection.

    See the doc of the patch function for details about what it does.

    Rturns:
        An object representing the patch. see:
        https://python-aspectlib.readthedocs.io/en/latest/testing.html?highlight=rollback#spy-mock-toolkit-record-mock-decorators
    """

    return aspectlib.weave(
        BaseDatabaseWrapper.ensure_connection, ensure_connection
    )


@contextmanager
def patch_ensure_connection_contextual():
    """Monkey patch BaseDatabaseWrapper.ensure_connection for the duration of
    the context."""

    patch = patch_ensure_connection()

    try:
        yield patch
    finally:
        patch.rollback()
