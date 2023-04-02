from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS
from sqlmodel import SQLModel

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


def configure_session(db_url: str, create_schema: bool = False):
    engine = create_engine(
        db_url, pool_size=4, max_overflow=0, echo=True
    )
    if create_schema:
        SQLModel.metadata.create_all(bind=engine)
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return session_local


@contextmanager
def session_manager(db_url: str = SQLALCHEMY_DATABASE_URL, create_schema: bool = False):
    SessionLocal = configure_session(db_url, create_schema)
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

