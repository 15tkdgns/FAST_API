# router로 app.include_router로 추가

from fastapi import FastAPI
from database import Base, engine
from starlette.middleware.sessions import SessionMiddleware

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_middleware(SessionMiddleware,secret_key = "session_secret")