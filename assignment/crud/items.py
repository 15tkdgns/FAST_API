from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from assignment.models import Item
from assignment.schemas import ItemCreate

    # id INT AUTO_INCREMENT PRIMARY KEY,
    # order_id INT NOT NULL,
    # book_id INT NOT NULL,
    # quantity INT NOT NULL DEFAULT 1,
    # price DECIMAL(10, 2) NOT NULL,
    # FOREIGN KEY (order_id) REFERENCES orders(id),
    # FOREIGN KEY (book_id) REFERENCES book(id)


class OrderCrud:
  # Create
  @staticmethod
  def create_item(item:ItemCreate, db:Session):
    new_item = Item(**item.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return {"msg", "아이템이 추가되었습니다"}
  
  # Read

  
  # Update
  @staticmethod
  def update_item(item_id:int, quantity:int, db:Session):
    item = db.execute(select(Item).filter(Item.id == item_id))
    if not item:
      raise HTTPException(status_code=404, detail='아이템 확인 불가')
    item.quantity = quantity
    db.commit()
    db.refresh(item)
    return {"msg":"수정되었습니다"}
  
  # Delete
  @staticmethod
  def delete_item(item_id:int, db:Session):
    item = db.execute(select(Item).filter(Item.id == item_id))
    if not item:
      raise HTTPException(status_code=404, detail="아이템 확인 불가")
    db.delete(item)
    db.commit()
    return {"msg":"삭제되었습니다"}