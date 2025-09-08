from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from assignment.models import Orders
from assignment.schema import OrderCreate

router = APIRouter(prefix='/orders')