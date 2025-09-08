from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from assignment.models import User
from assignment.schema import UserCreate

router = APIRouter(prefix='/users')

# 신규 유저 추가
@router.post("/")
def create_user(user:UserCreate, db:Session=Depends()):
  exist = db.query(User).filter(User.username == user.username).first()
  if exist:
    raise HTTPException(status_code=404, detail='이미 존재하는 유저입니다')
  new_user = User(username=user.username, password=user.password, email=user.email)
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return {"msg": "유저가 추가되었습니다"}

# 유저 읽기
@router.get("/")
def get_users(db:Session=Depends()):
  return db.query(User).all()

# 유저 정보 수정
@router.put("/{id}")
def update_user(update:UserCreate, id:int, db:Session=Depends()):
  user = db.query(User).filter(User.id == id).first()
  if not user:
    raise HTTPException(status_code=404, detail="확인 불가합니다")
  user.username = update.username
  user.password = update.password
  user.email = update.email
  db.commit()
  db.refresh(user)
  return {"msg": "유저정보가 수정되었습니다"}

# 유저 삭제
@router.delete("/{id}")
def delete_user(id:int, db:Session=Depends()):
  user = db.query(User).filter(User.id == id).first()
  if not user:
    raise HTTPException(status_code=404, detail="유저 확인 불가")
  db.delete(user)
  db.commit()
  return {"msg": "유저가 삭제되었습니다"}
