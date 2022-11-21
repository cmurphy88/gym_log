from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from .. import db
from . import schema
from . import services

router = APIRouter(tags=['Exercise'], prefix='/exercise')


@router.post('/new', status_code=status.HTTP_201_CREATED)
async def create_new_exercise(request: schema.Exercise, database: Session = Depends(db.get_db)):
    return await services.create_new_exercise(request, database)


@router.get('/exercises', response_model=List[schema.DisplayExercise])
async def get_all_exercises(database: Session = Depends(db.get_db)):
    return await services.get_all_exercises(database)


@router.get('/{id}', response_model=schema.DisplayExercise)
async def get_exercise(exercise_id: int, database: Session = Depends(db.get_db)):
    return await services.get_exercise(exercise_id, database)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_exercise(request: schema.UpdateExercise, database: Session = Depends(db.get_db)):
    return await services.update_exercise(request, database)


@router.delete('/{id}', status_code=status.HTTP_200_OK, response_class=Response)
async def delete_exercise(exercise_id: int, database: Session = Depends(db.get_db)):
    return await services.delete_exercise(exercise_id, database)
