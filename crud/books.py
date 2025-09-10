from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from model import Book
from schemas import BookCreate

class BookCrud:
  # Create - 도서 생성
  @staticmethod
  def create_book(book:BookCreate, db:Session) -> Book:
    exist = db.execute(select(Book).filter(Book.title == book.title)).scalars().first()
    if exist:
      raise HTTPException(status_code=404, detail='이미 존재하는 타이틀 입니다')
    new_book = Book(**book.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return {"msg":f"{book.title} 도서 정보가 추가되었습니다"}

  # Read - 도서 전체 조회
  @staticmethod
  def get_books(db:Session):
    all_books = db.execute(select(Book)).scalars().all()
    return all_books

  # Update - 도서 정보 수정 / router에 연결 할 때 '/{book_id}'로 작업
  @staticmethod
  def update_book(book_id:int, update:BookCreate, db:Session):
    book = db.execute(select(Book).filter(Book.id == book_id)).scalars().first()
    if not book:
      raise HTTPException(status_code=404, detail="확인 불가")
    book.title = update.title
    book.author = update.author
    book.pub_date = update.pub_date
    book.price = update.price
    db.commit()
    db.refresh(book)
    return {"msg":"도서 정보가 수정되었습니다"}

  # Delete - 도서 정보 삭제 / router에 연결 할 때 query로 타이틀 넣으면 삭제
  @staticmethod
  def delete_book(title:str, db:Session):
    book = db.execute(select(Book).filter(Book.title == title)).scalars().first()
    if not book:
      raise HTTPException(status_code=404, detail = "도서 확인 불가")
    db.delete(book)
    db.commit()
    return {"msg":"도서 정보가 삭제되었습니다"}