from fastapi import APIRouter, Depends, Path, Query
from sqlalchemy.orm import Session
from crud.books import BookCrud
from schemas import BookCreate
from database import get_db

router = APIRouter(prefix="/book",tags=['Books'])
