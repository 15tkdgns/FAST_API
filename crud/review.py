from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from model import Review
from schemas import ReviewCreate

class ReviewCrud:
  # Create - 리뷰 생성
  @staticmethod
  def create_review(review:ReviewCreate, db:Session):
    new_review = Review(**review.model_dump())
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return {"msg":"리뷰가 생성되었습니다"}
  
  # Read
  @staticmethod
  def get_reviews(db:Session):
    all_reviews = db.execute(select(Review)).scalars().all()
    return all_reviews
  
  # Update
  @staticmethod
  def update_review(review_id:int, update:ReviewCreate, db:Session):
    review = db.execute(select(Review).filter(Review.id == review_id)).scalars().first()
    if not review:
      raise HTTPException(status_code=404, detail='리뷰 확인 불가')
    Review.user_id = update.user_id
    Review.book_id = update.book_id
    Review.rating = update.rating
    Review.comment = update.comment
    db.commit()
    db.refresh(update)
    return {"msg":"리뷰가 수정되었습니다"}

  # Delete
  @staticmethod
  def delete_review(review_id:int, db:Session):
    review = db.execute(select(Review).filter(Review.id == review_id)).scalars().first()
    if not review:
      raise HTTPException(status_code=404, detail="리뷰 확인 불가")
    db.delete(review)
    db.commit()
    return {"msg":"리뷰가 삭제되었습니다"}