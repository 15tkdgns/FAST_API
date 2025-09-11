from typing import Optional
from fastapi import APIRouter, Depends, Path, Query, HTTPException
from sqlalchemy.orm import Session
from crud.books import BookCrud
from schemas import BookCreate
from database import get_db

router = APIRouter(prefix="/book", tags=["Books"])

@router.post("/create")
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return BookCrud.create_book(book, db) # 생성

@router.get("/list")
def list_books(
    author: Optional[str] = Query(None, min_length=1, description="저자명 필터"),
    min_price: Optional[float] = Query(None, ge=0, description="최소 가격"),
    max_price: Optional[float] = Query(None, ge=0, description="최대 가격"),
    db: Session = Depends(get_db),
):
    books = BookCrud.get_books(db) # 전체 조회
    if author is not None:
        books = [b for b in books if b.author == author]
    if min_price is not None:
        books = [b for b in books if float(b.price) >= float(min_price)]
    if max_price is not None:
        books = [b for b in books if float(b.price) <= float(max_price)]
    return books # 필터링 목록

@router.get("/detail/{book_id}")
def get_book(book_id: int = Path(..., ge=1), db: Session = Depends(get_db)):
# 필요 시 CRUD에 전용 메서드 추가 권장
    books = BookCrud.get_books(db) # 전체 조회
    match = next((b for b in books if b.id == book_id), None)
    if not match:
        raise HTTPException(status_code=404, detail="도서 확인 불가")
    return match # 단건

@router.put("/update/{book_id}")
def update_book(
    book_id: int = Path(..., ge=1),
    update: BookCreate = ...,
    db: Session = Depends(get_db),
    ):
    return BookCrud.update_book(book_id, update, db) # 수정

@router.delete("/delete")
def delete_book(title: str = Query(..., min_length=1), db: Session = Depends(get_db)):
    return BookCrud.delete_book(title, db) # 삭제
