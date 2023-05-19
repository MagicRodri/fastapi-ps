from typing import Generator

from core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_engine():
    return create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)

def get_session():
    engine = get_engine()
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return session_local()

def get_db() -> Generator:
    try:
        db = get_session()
        yield db
    finally:
        db.close()