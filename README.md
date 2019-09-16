# Django Database Connection Retrier

[![License](https://img.shields.io/:license-mit-blue.svg)](http://doge.mit-license.org)
[![PyPi](https://badge.fury.io/py/django-db-connection-retrier.svg)](https://pypi.python.org/pypi/django-db-connection-retrier)

Automatically try to re-establish Django database connections when they fail due to DNS errors.

---

When the Django app (`dbconnectionretrier`) loads, a hook is installed in Django's [`BaseDatabaseWrapper.ensure_connection`](https://github.com/django/django/blob/master/django/db/backends/base/base.py#L216) that catches `django.db.OperationalError`. If the error raised is a DNS error, the connction attempt is retried synchronously **three times**.

## Installation
1. Install the package from PyPi:

        $ pip install django-db-connection-retrier

2. Add `dbconnectionretrier` to your `INSTALLED_APPS`:

        INSTALLED_APPS = [
            'dbconnectionretrier',
            ...
        ]

## Manual usage
Adding `dbconnectionretrier` to `INSTALLED_APPS` enables automatic connection retrying. Want more granular control over patching?

### Globally
```
from dbconnectionretrier.patch import patch_ensure_connection

# after this line executes, connection retrying is enabled
patch = patch_ensure_connection()

# after this line, the connection retrying is disabled
patch.rollback()
```

### Context manager
```
from dbconnectionretrier.patch import patch_ensure_connection_contextual

with patch_ensure_connection_contextual():
    # all code inside this block benefits from connectiion retrying
```
