from matplotlib.pyplot import connect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings
from typing import Generator

# Uncomment the following lines to use Postgres instead of SQLite
# SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

SQLALCHEMY_DATABASE_URL = "sqlite:///./app.sqlite"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})  

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

def get_db() -> Generator[SessionLocal, None, None]:
    """
    Returns a database session
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close() 