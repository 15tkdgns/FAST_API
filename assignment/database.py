from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .crud.SQLAlchemy_ORM import Base

DATABASE_CONN = "mysql+mysqlconnector://root:12345@127.0.0.1:3306/board"

engine = create_engine(
    DATABASE_CONN
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
