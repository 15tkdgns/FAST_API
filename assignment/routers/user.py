from fastapi import APIRouter, Depends, Path, Query
from sqlalchemy.orm import Session
from assignment.crud.users import UserCrud
from assignment.schemas import UserCreate
from assignment.database import get_db

router = APIRouter(prefix="/user",tags=['Users'])

# post
@router.post("/")
def create_user(user:UserCreate, db:Session = Depends(get_db)):
  return UserCrud.create_user(user, db)

# get / 유저 id 값 가져와서 조회
@router.get("/{user_id}")
def get_user(user_id:int=Path(..., ge=1), db:Session = Depends(get_db)):
  return UserCrud.get_user(user_id, db)

# put / 유저 id 값 가져와서 수정
@router.put("/{user_id}")
def update_user(user_id:int = Path(..., ge=1), update:UserCreate|None=None, db:Session = Depends(get_db)):
  return UserCrud.update_user(user_id, update, db)

# @router.delete("/")
