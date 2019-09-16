from io import StringIO
from logging import StreamHandler

import pytest

from django.db import OperationalError
from django.db.utils import load_backend

from dbconnectionretrier.apps import DBConnectionRetrierConfig
from dbconnectionretrier.ensure_connection import LOGGER


def test_app_config_install_patch(unknown_host):
    """Tests whether the Django app config properly installs the retrier and
    retries connection failures."""

    try:
        patch = DBConnectionRetrierConfig.ready(None)

        io = StringIO()
        LOGGER.addHandler(StreamHandler(io))
        with pytest.raises(OperationalError):
            backend = load_backend(unknown_host["ENGINE"])
            conn = backend.DatabaseWrapper(unknown_host, "unknown_host")
            conn.ensure_connection()

        # test that retrying has taken place (DNS errors might have been fixed)
        assert "trial 0" in io.getvalue()
    finally:
        patch.rollback()
