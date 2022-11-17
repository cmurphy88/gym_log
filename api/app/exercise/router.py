from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from .. import db
from . import schema
from . import services

router = APIRouter(tags=['Exercise'], prefix='/exercise')


@router.get('/', response_model=List[schema.DisplayExercise])
async def get_all_exercises(database: Session = Depends(db.get_db)):
    return await services.get_all_exercises(database)
