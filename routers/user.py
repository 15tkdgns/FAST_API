from fastapi import APIRouter, Depends, Path, Query
from sqlalchemy.orm import Session
from crud.users import UserCrud
from schemas import UserCreate
from database import get_db

router = APIRouter(prefix="/user",tags=['Users'])

# post
@router.post("/create")
def create_user(user:UserCreate, db:Session = Depends(get_db)):
  return UserCrud.create_user(user, db)

# get / 유저 id 값 가져와서 조회
@router.get("/list/{user_id}")
def get_user(user_id:int=Path(..., ge=1), db:Session = Depends(get_db)):
  return UserCrud.get_user(user_id, db)

# put / 유저 id 값 가져와서 수정
@router.put("/update/{user_id}")
def update_user(user_id:int = Path(..., ge=1), update:UserCreate|None=None, db:Session = Depends(get_db)):
  return UserCrud.update_user(user_id, update, db)

# @router.delete("/")
@router.delete("/delete")
def delete_user(
  username: str = Query(..., min_length=1),
  db: Session = Depends(get_db),
  ):
  return UserCrud.delete_user(username, db)
