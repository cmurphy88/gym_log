from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from .. import db
from . import schema
from . import services

router = APIRouter(tags=['Workout'], prefix='/workouts')


@router.post('/new', status_code=status.HTTP_201_CREATED)
async def create_new_workout(request: schema.Workout, database: Session = Depends(db.get_db)):
    return await services.create_new_workout(request, database)


@router.get('/all', response_model=List[schema.DisplayWorkout])
async def get_all_workouts(database: Session = Depends(db.get_db)):
    return await services.get_all_workouts(database)


@router.get('/{id}', response_model=schema.DisplayWorkout)
async def get_workout_by_id(workout_id: int, database: Session = Depends(db.get_db)):
    return await services.get_workout_by_id(workout_id, database)


# @router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
# async def update_exercise(request: schema.UpdateExercise, database: Session = Depends(db.get_db)):
#     return await services.update_exercise(request, database)


@router.delete('/{id}', status_code=status.HTTP_200_OK, response_class=Response)
async def delete_workout(workout_id: int, database: Session = Depends(db.get_db)):
    return await services.delete_workout(workout_id, database)
