from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from assignment.models import Item
from assignment.schema import ItemCreate


router = APIRouter(prefix='/items')