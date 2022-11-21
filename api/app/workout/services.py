from typing import List, Optional
from fastapi import HTTPException, status
from . import models


async def create_new_workout(request, database) -> models.Workout:
    new_workout = models.Workout(name=request.name, user_id=request.user_id)
    database.add(new_workout)
    database.commit()
    database.refresh(new_workout)
    return new_workout


async def get_all_workouts(database) -> List[models.Workout]:
    workouts = database.query(models.Workout).all()
    return workouts


async def get_workout_by_id(workout_id, database):
    return None


async def delete_workout(workout_id, database):
    return None
