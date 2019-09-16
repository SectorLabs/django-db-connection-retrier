# Django Database Connection Retrier

Automatically try to re-establish Django database connections when they fail due to DNS lookup errors.

## Installation
1. Install the package from PyPi:

        $ pip install django-db-connection-retrier

2. Add `dbconnectionretrier` to your `INSTALLED_APPS`:

        INSTALLED_APPS = [
            'dbconnectionretrier',
            ...
        ]
