# router로 app.include_router로 추가
from fastapi import FastAPI
from database import Base, engine
from starlette.middleware.sessions import SessionMiddleware
from routers import user
from SQLAlchemy_ORM import User

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_middleware(SessionMiddleware,secret_key = "session_secret")

app.include_router(user.router)