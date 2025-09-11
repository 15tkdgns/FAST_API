from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from crud.review import ReviewCrud
from schemas import ReviewCreate
from database import get_db

router = APIRouter(prefix="/review", tags=["Reviews"])

@router.post("/")
def create_review(review: ReviewCreate, db: Session = Depends(get_db)):
  return ReviewCrud.create_review(review, db) # 생성

@router.get("/")
def get_reviews(db: Session = Depends(get_db)):
  return ReviewCrud.get_reviews(db) # 전체 조회

@router.put("/{review_id}")
def update_review(
review_id: int = Path(..., ge=1),
update: ReviewCreate | None = None,
db: Session = Depends(get_db),
):
  return ReviewCrud.update_review(review_id, update, db) # 수정

@router.delete("/{review_id}")
def delete_review(review_id: int = Path(..., ge=1), db: Session = Depends(get_db)):
  return ReviewCrud.delete_review(review_id, db) # 삭제
