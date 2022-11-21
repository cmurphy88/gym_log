from typing import List, Optional
from fastapi import HTTPException, status
from . import models


async def create_new_exercise(request, database) -> models.Exercise:
    new_exercise = models.Exercise(name=request.name)
    database.add(new_exercise)
    database.commit()
    database.refresh(new_exercise)
    return new_exercise


async def get_all_exercises(database) -> List[models.Exercise]:
    exercises = database.query(models.Exercise).all()
    return exercises


async def get_exercise(exercise_id, database) -> models.Exercise:
    exercise = database.query(models.Exercise).get(exercise_id)
    return exercise


# async def update_exercise(request, database) -> models.Exercise:
#     old_exercise = database.query(models.Exercise).get(request.id)
#     if not old_exercise:
#         raise status.HTTP_404_NOT_FOUND
#     request_data = request.dict(exclude_unset=True)
# try and do a delete, and create a new exercise???


async def delete_exercise(exercise_id, database):
    database.query(models.Exercise).filter(models.Exercise.id == exercise_id)
    database.commit()
