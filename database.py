from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase

from config import Settings

engine = create_engine(Settings.database_url)

session_local = sessionmaker(bind = engine, autoflush = False)

class Base(DeclarativeBase):
    pass

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()