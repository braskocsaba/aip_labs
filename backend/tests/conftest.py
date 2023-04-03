import pytest

from db import session_manager
from config import DB_HOST_TEST, DB_NAME, DB_USER, DB_PORT, DB_PASS

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST_TEST}:{DB_PORT}/{DB_NAME}"


@pytest.fixture()
def db_session_test():
    with session_manager(SQLALCHEMY_DATABASE_URL, create_schema=True) as db:
        yield db
