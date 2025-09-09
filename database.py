from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from SQLAlchemy_ORM import Base

DATABASE_CONN = "mysql+mysqlconnector://root:gkxogh11%40@127.0.0.1:3306/board"

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
