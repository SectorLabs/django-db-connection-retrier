from io import StringIO
from logging import StreamHandler

import pytest

from django.db import OperationalError
from django.db.utils import load_backend

from dbconnectionretrier.ensure_connection import LOGGER
from dbconnectionretrier.patch import patch_ensure_connection_contextual


@patch_ensure_connection_contextual()
def test_reconnect_failed(unknown_host):
    """For an unknown host, connection has to be retried.

    Behavior validation is done by intercepting the logging messages
    """
    io = StringIO()
    LOGGER.addHandler(StreamHandler(io))
    with pytest.raises(OperationalError):
        backend = load_backend(unknown_host["ENGINE"])
        conn = backend.DatabaseWrapper(unknown_host, "unknown_host")
        conn.ensure_connection()
    # test that retrying has taken place (DNS errors might have been fixed)
    assert "trial 0" in io.getvalue()


@patch_ensure_connection_contextual()
def test_connect_failed_missing_db(unknown_db):
    """An unknown database must not trigger retrying, it should just fail.

    Behavior validation is done by intercepting the logging messages
    """
    io = StringIO()
    LOGGER.addHandler(StreamHandler(io))
    with pytest.raises(OperationalError):
        backend = load_backend(unknown_db["ENGINE"])
        conn = backend.DatabaseWrapper(unknown_db, "unknown_db")
        conn.ensure_connection()

    # test that retrying has NOT taken place (there's no point)
    assert "trial 0" not in io.getvalue()
