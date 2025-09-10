from sqlalchemy import (
    Column, Integer, String, Date, DateTime,
    ForeignKey, DECIMAL, Text
)
from sqlalchemy.sql import func
from database import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    author = Column(String(100), nullable=False)
    pub_date = Column(Date, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    order_date = Column(DateTime, server_default=func.now()) # 디폴트 현재시간
    total_price = Column(DECIMAL(10, 2), nullable=False)

class Item(Base):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("book.id"), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    price = Column(DECIMAL(10, 2), nullable=False)

class Review(Base):
    __tablename__ = "review"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("book.id"), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(Text)
    created_at = Column(DateTime, server_default=func.now()) # 디폴트 현재시간
