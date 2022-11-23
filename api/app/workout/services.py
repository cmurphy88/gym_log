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


async def get_workout_by_id(workout_id, database) -> models.Workout:
    workout = database.query(models.Workout).get(workout_id)
    return workout


async def get_all_users_workouts(user_id, database) -> List[models.Workout]:
    workouts = database.query(models.Workout).filter(models.Workout.user_id == user_id)
    workout_list = list()
    for x in workouts:
        workout_list.append(x)
    return workout_list


async def delete_workout(workout_id, database):
    database.query(models.Workout).filter(models.Workout.id == workout_id)
    database.commit()
