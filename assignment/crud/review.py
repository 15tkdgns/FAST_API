from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from assignment.models import Review
from assignment.schema import ReviewCreate

router = APIRouter(prefix='/reviews')
