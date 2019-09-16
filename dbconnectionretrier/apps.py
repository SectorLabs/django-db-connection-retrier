from django.apps import AppConfig

from .patch import patch_ensure_connection


class DBConnectionRetrierConfig(AppConfig):
    """Django app configuration that hooks.

    :see:BaseDatabaseWrapper.ensure_connection to automatically retry
    connection failures.
    """

    name = "dbconnectionretrier"

    def ready(self):
        return patch_ensure_connection()
