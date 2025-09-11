from fastapi import APIRouter, Depends, Path, Query
from sqlalchemy.orm import Session
from crud.orders import OrderCrud
from schemas import OrderCreate
from database import get_db

router = APIRouter(prefix="/order", tags=["Orders"])

@router.post("/create")
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
  return OrderCrud.create_order(order, db) # 생성

@router.get("/detail/{order_id}")
def get_order(order_id: int = Path(..., ge=1), db: Session = Depends(get_db)):
  return OrderCrud.get_order(order_id, db) # 단건 조회

@router.put("/update/{order_id}")
def update_order_price(
  order_id: int = Path(..., ge=1),
  price: float = Query(..., gt=0),
  db: Session = Depends(get_db),
):
  return OrderCrud.update_order_price(order_id, price, db) # 가격 수정

@router.delete("/delete/{order_id}")
def delete_order(order_id: int = Path(..., ge=1), db: Session = Depends(get_db)):
  return OrderCrud.delete_order(order_id, db) # 삭제



