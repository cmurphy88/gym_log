from typing import List, Optional
from fastapi import HTTPException, status
from . import models


async def get_all_exercises(database) -> List[models.Exercise]:
    exercises = database.query(models.Exercise).all()
    return exercises


async def get_exercise(exercise_id, database) -> models.Exercise:
    exercise = database.query(models.Exercise).get(exercise_id)
    return exercise


def update_exercise(request, database):
    return None


def delete_exercise(exercise_id, database):
    database.query(models.Exercise).filter(models.Exercise.id == exercise_id).delete()
