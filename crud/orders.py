from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from SQLAlchemy_ORM import Order
from schemas import OrderCreate

class OrderCrud:
  # Create - 주문정보 생성
  @staticmethod
  def create_order(order:OrderCreate, db:Session):
    new_order = Order(**order.model_dump())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return {"msg":"주문 정보가 추가되었습니다"}
  
  # Read - 아이디에 맞는 주문 정보 조회 / '/{order_id} 로 작업'
  @staticmethod
  def get_order(order_id:int, db:Session):
    order_data = db.execute(select(Order).filter(Order.id == order_id)).scalars().first()
    if not order_data:
      raise HTTPException(status_code=404, detail="주문 정보 확인 불가")
    return order_data
  
  # Update - 가격만 수정가능
  @staticmethod
  def update_order_price(order_id:int, price:float, db:Session):
    order = db.execute(select(Order).filter(Order.id == order_id)).scalars().first()
    if not order:
      raise HTTPException(status_code=404, detail="주문 정보 확인 불가")
    order.total_price = price
    db.commit()
    db.refresh()
    return {"msg":f"{order.id}의 주문가격을 변경했습니다"}
  
  # delete
  @staticmethod
  def delete_order(order_id:int, db:Session):
    order = db.execute(select(Order).filter(Order.id == order_id)).scalars().first()
    
    db.delete(order)
    db.commit()
    return {"msg":"주문 정보가 삭제되었습니다"}