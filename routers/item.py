from fastapi import APIRouter, Depends, Path, Query
from sqlalchemy.orm import Session
from crud.items import OrderCrud as ItemCrud # 내부 클래스명이 OrderCrud로 되어 있어 임시로 별칭 적용
from schemas import ItemCreate
from database import get_db

router = APIRouter(prefix="/item", tags=["Items"])

@router.post("/")
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
  return ItemCrud.create_item(item, db) # 생성

@router.get("/")
def get_items(db: Session = Depends(get_db)):
  return ItemCrud.get_items(db) # 전체 조회

@router.put("/{item_id}")
def update_item(
item_id: int = Path(..., ge=1),
quantity: int = Query(..., ge=1),
db: Session = Depends(get_db),
):
  return ItemCrud.update_item(item_id, quantity, db) # 수량 변경

@router.delete("/{item_id}")
def delete_item(item_id: int = Path(..., ge=1), db: Session = Depends(get_db)):
  return ItemCrud.delete_item(item_id, db) # 삭제
