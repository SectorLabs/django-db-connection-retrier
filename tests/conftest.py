import dj_database_url
import pytest


def set_defaults(db):
    """Set the mandatory settings on the connection."""
    db.setdefault("TIME_ZONE", None)
    db.setdefault("CONN_MAX_AGE", None)
    db.setdefault("OPTIONS", {})
    db.setdefault("ATOMIC_REQUESTS", True)


@pytest.fixture()
def unknown_host():
    """DB connection with a broken host name."""
    db = dj_database_url.config(
        default="postgres://this_domain_should_not_exist/test_mydb"
    )
    set_defaults(db)
    return db


@pytest.fixture()
def unknown_db():
    """DB connection with a broken database name."""
    db = dj_database_url.config(default="postgres:///this_db_should_not_exist")
    set_defaults(db)
    return db
