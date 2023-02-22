from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from .. import db
from . import schema
from . import services

router = APIRouter(tags=['Set'], prefix='/sets')


@router.post('/new', status_code=status.HTTP_201_CREATED)
async def create_new_set(request: schema.Set, database: Session = Depends(db.get_db)):
    return await services.create_new_set(request, database)


@router.get('/all', response_model=List[schema.DisplaySet])
async def get_all_sets(database: Session = Depends(db.get_db)):
    return await services.get_all_sets(database)


@router.get('/{id}', response_model=schema.DisplaySet)
async def get_set_by_id(set_id: int, database: Session = Depends(db.get_db)):
    return await services.get_set_by_id(set_id, database)


@router.get('/exercise/{exercise_id}', response_model=List[schema.DisplaySet])
async def get_all_exercise_sets(exercise_id: int, database: Session = Depends(db.get_db)):
    return await services.get_all_exercise_sets(exercise_id, database)


@router.get('/workout/{workout_id}', response_model=List[schema.DisplaySet])
async def get_all_workout_sets(workout_id: int, database: Session = Depends(db.get_db)):
    return await services.get_all_workout_sets(workout_id, database)


@router.get('/date/{exercise_id}', response_model=List[schema.SetWithDate])
async def get_set_date(exercise_id: int, database: Session = Depends(db.get_db)):
    return await services.get_set_date(exercise_id, database)


# @router.get('/users/{id}', response_model=List[schema.DisplaySet])
# async def get_all_users_sets(user_id: int, database: Session = Depends(db.get_db)):
#     return await services.get_all_users_sets(user_id, database)


# @router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
# async def update_exercise(request: schema.UpdateExercise, database: Session = Depends(db.get_db)):
#     return await services.update_exercise(request, database)


@router.delete('/{id}', status_code=status.HTTP_200_OK, response_class=Response)
async def delete_set(set_id: int, database: Session = Depends(db.get_db)):
    return await services.delete_set(set_id, database)
