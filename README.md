# Django Database Connection Retrier

[![License](https://img.shields.io/:license-mit-blue.svg)](http://doge.mit-license.org)
[![PyPi](https://badge.fury.io/py/django-db-connection-retrier.svg)](https://pypi.python.org/pypi/django-db-connection-retrier)

Automatically try to re-establish Django database connections when they fail due to DNS lookup errors.

## Installation
1. Install the package from PyPi:

        $ pip install django-db-connection-retrier

2. Add `dbconnectionretrier` to your `INSTALLED_APPS`:

        INSTALLED_APPS = [
            'dbconnectionretrier',
            ...
        ]
