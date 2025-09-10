# DATABASE_CONN 주소 본인 비밀번호에 맞춰서 작성 후 작업. 작업 완료하시면 주석처리 해주세요!

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_CONN = "mysql+mysqlconnector://root:12345@127.0.0.1:3306/board"
# DATABASE_CONN = "mysql+mysqlconnector://root:gkxogh11%40@127.0.0.1:3306/practice"

engine = create_engine(DATABASE_CONN)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
