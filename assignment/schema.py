from pydantic import BaseModel
from datetime import date

class UserCreate(BaseModel):
  username:str
  password:str
  email:str

class BookCreate(BaseModel):
  title:str
  author:str
  pub_date:date
  price:float

class OrderCreate(BaseModel):
  user_id:int
  total_price:float

class ItemCreate(BaseModel):
  order_id:int
  book_id:int
  quantity:int
  price:float

class ReviewCreate(BaseModel):
  user_id:int
  book_id:int
  rating:int
  comment:str|None = None