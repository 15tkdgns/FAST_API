from sqlalchemy import Column, Integer, String, Date, DECIMAL
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
  __tablename__ = "user"
  id = Column(Integer, primary_key=True, index=True, autoincrement=True)
  username = Column(String(50), unique=True, nullable=False)
  password = Column(String(255), nullable=False)
  email = Column(String(100), unique=True, nullable=False)

class Book(Base):
  __tablename__ = "book"
  id = Column(Integer, primary_key=True, index=True, autoincrement=True)
  title = Column(String(255), nullable=False)
  author = Column(String(100), nullable=False)
  pub_date = Column(Date, nullable=False)
  price = Column(DECIMAL(10,2), nullable=False)