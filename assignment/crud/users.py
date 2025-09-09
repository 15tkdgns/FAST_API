from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from assignment.models import User
from assignment.schemas import UserCreate

class UserCrud:
  # Create - 유저 생성
  @staticmethod
  def create_user(user:UserCreate, db:Session) -> User:
    exist = db.execute(select(User).filter(User.username == user.username)).scalars().first()
    if exist:
      raise HTTPException(status_code=404, detail='이미 존재하는 유저입니다')
    new_user = User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"msg":f"{user.username}님이 추가되었습니다"}

  # Read - id 값으로 유저 정보 조회 router에 연결 할 때 '/{user_id}'로 작업
  @staticmethod
  def get_user(user_id:int, db:Session):
    user_info = db.execute(select(User).filter(User.id == user_id)).scalars().first()
    return user_info

  # Update - 유저 정보 수정 / router에 연결 할 때 '/{user_id}'로 작업
  @staticmethod
  def update_user(user_id:int, update:UserCreate, db:Session):
    user = db.execute(select(User).filter(User.id == user_id)).scalars().first()
    if not user:
      raise HTTPException(status_code=404, detail="확인 불가")
    user.username = update.username
    user.password = update.password
    user.email = update.email
    db.commit()
    db.refresh(user)
    return {"msg":f"{user.username}님의 회원정보가 수정되었습니다"}

  # Delete - 유저 정보 삭제 / router에 연결 할 때 query로 유저 네임 넣으면 삭제
  @staticmethod
  def delete_user(username:str, db:Session):
    user = db.execute(select(User).filter(User.username == username)).scalars().first()
    if not user:
      raise HTTPException(status_code=404, detail = "유저 확인 불가")
    db.delete(user)
    db.commit()
    return {"msg":"유저 정보가 삭제되었습니다"}
