from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta, timezone, datetime
import jwt
from database import get_db

app=FastAPI()

# JWT 설정
SECRET_KEY="secret_key"
oauth_scheme=OAuth2PasswordBearer(tokenUrl="token")

# 토큰 생성
def create_token(data:dict, expire:timedelta|None=None)->str:
    exp=datetime.now(timezone.utc)+timedelta(minutes=60)
    data['exp']=exp
    return jwt.encode(data, SECRET_KEY, algorithm="HS256")

# 토큰 검증
def verify_token(token:str)->str:
    try:
        payload=jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        username:str=payload.get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload")
        return username
    except Exception:
        raise

# 토큰 발급 엔드포인트
@app.post("/token")
def token(f_data:OAuth2PasswordRequestForm=Depends(), db:Session=Depends(get_db)):
    user=db.get(f_data.username)
    if not user or user['password'] != f_data.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token")
    access_token=create_token(data={"sub":user['username']},
                              expire=timedelta(minutes=60))
    return {"access_token":access_token, "token_type":"bearer"}
    

# 토큰 검증 엔드포인트
@app.post("/verify")
def verify(token:str=Depends(oauth_scheme)):
    username=verify_token(token)
    return {"msg":"Valid Token"}