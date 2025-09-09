from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from assignment.models import Book
from assignment.schema import BookCreate

router = APIRouter(prefix='/books')

# 책 추가
@router.post('/')
def create_book(book:BookCreate, db:Session=Depends()):
  same_title = db.query(Book).filter(Book.title == book.title).first()
  if same_title:
    raise HTTPException(status_code=404, detail="같은 제목은 추가 불가합니다")
  new_book = Book(title=book.title, author=book.author, pub_date=book.pub_date, price=book.price)
  db.add(new_book)
  db.commit()
  db.refresh(new_book)
  return {"msg": "책 추가되었습니다"}

# 책 조회 all
@router.get("/")
def get_books(db:Session=Depends()):
  return db.query(Book).all()

# 책 정보 수정
@router.put("/{id}")
def update_user(update:BookCreate, id:int, db:Session=Depends()):
  book = db.query(Book).filter(Book.id == id).first()
  if not book:
    raise HTTPException(status_code=404, detail="확인 불가합니다")
  book.title = update.title
  book.author = update.author
  book.pub_date = update.pub_date
  book.price = update.price
  db.commit()
  db.refresh(book)
  return {"msg": "책 정보가 수정되었습니다"}

# 책 삭제
@router.delete("/{id}")
def delete_book(id:int, db:Session=Depends()):
  book = db.query(Book).filter(Book.id == id).first()
  if not book:
    raise HTTPException(status_code=404, detail="유저 확인 불가")
  db.delete(book)
  db.commit()
  return {"msg": "책 정보가 삭제되었습니다"}
