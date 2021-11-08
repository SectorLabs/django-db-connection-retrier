import django

if django.VERSION < (3, 2):  # pragma: nocover
    default_app_config = "dbconnectionretrier.apps.DBConnectionRetrierConfig"
