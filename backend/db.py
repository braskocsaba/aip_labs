from contextlib import contextmanager

from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS
from sqlmodel import SQLModel, Session, create_engine
from models import Coupon
from models import Action

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def configure_session(db_url: str, create_schema: bool = False):
    engine = create_engine(db_url)
    if create_schema:
        SQLModel.metadata.create_all(bind=engine)
    session_local = Session(bind=engine)
    return session_local


@contextmanager
def session_manager(db_url: str = SQLALCHEMY_DATABASE_URL, create_schema: bool = False):
    session = configure_session(db_url, create_schema)
    try:
        yield session
    finally:
        session.close()

def create_db(db_url: str = SQLALCHEMY_DATABASE_URL, create_schema: bool = True):
    print("Creating db...........")
    configure_session(db_url, create_schema)

create_db()
