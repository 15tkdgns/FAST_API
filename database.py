from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# user, password, name 각각 본인 sql에 맞춰서 설정 후 실행
DB_USER = 'root'
DB_PASSWORD = '12345'
DB_NAME = 'board'
DATABASE_CONN = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@127.0.0.1:3306/{DB_NAME}"

engine = create_engine(DATABASE_CONN)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
