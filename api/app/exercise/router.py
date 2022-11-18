from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from .. import db
from . import schema
from . import services

router = APIRouter(tags=['Exercise'], prefix='/exercise')


@router.get('/exercises', response_model=List[schema.DisplayExercise])
async def get_all_exercises(database: Session = Depends(db.get_db)):
    return await services.get_all_exercises(database)


@router.get('/{id}', response_model=schema.DisplayExercise)
async def get_workout(exercise_id: int, database: Session = Depends(db.get_db)):
    return await services.get_exercise(exercise_id, database)


@router.put('/{id}', status_code=status.HTTP_200_OK, response_class=Response)
async def get_workout(request: schema.Exercise, database: Session = Depends(db.get_db)):
    return await services.update_exercise(request, database)


@router.delete('/{id}', status_code=status.HTTP_200_OK, response_class=Response)
async def get_workout(exercise_id: int, database: Session = Depends(db.get_db)):
    return await services.delete_exercise(exercise_id, database)
