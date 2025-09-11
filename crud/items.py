from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from model import Item
from schemas import ItemCreate

class OrderCrud:
  # Create
  @staticmethod
  def create_item(item:ItemCreate, db:Session):
    new_item = Item(**item.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return {"msg", "상품이 추가되었습니다"}
  
  # Read
  @staticmethod
  def get_items(db:Session):
    all_items = db.execute(select(Item)).scalars().all()
    return all_items
  
  # Update
  @staticmethod
  def update_item(item_id:int, quantity:int, db:Session):
    item = db.execute(select(Item).filter(Item.id == item_id)).scalars().first()
    if not item:
      raise HTTPException(status_code=404, detail='상품 확인 불가')
    item.quantity = quantity
    db.commit()
    db.refresh(item)
    return {"msg":"상품 정보가 수정되었습니다"}
  
  # Delete
  @staticmethod
  def delete_item(item_id:int, db:Session):
    item = db.execute(select(Item).filter(Item.id == item_id)).scalars().first()
    if not item:
      raise HTTPException(status_code=404, detail="아이템 확인 불가")
    db.delete(item)
    db.commit()
    return {"msg":"상품이 삭제되었습니다"}