from typing import List, Optional
from fastapi import HTTPException, status
from . import models
from ..workout.models import WorkoutExercise

async def create_new_exercise(request, database) -> models.Exercise:
    new_exercise = models.Exercise(name=request.name)
    database.add(new_exercise)
    database.commit()
    database.refresh(new_exercise)
    return new_exercise


async def add_exercise_to_workout(request, database) -> WorkoutExercise:
    new_exercise_workout = WorkoutExercise(workout_id=request.workout_id, exercise_id=request.exercise_id)
    database.add(new_exercise_workout)
    database.commit()
    database.refresh(new_exercise_workout)
    return new_exercise_workout


async def get_all_exercises(database) -> List[models.Exercise]:
    exercises = database.query(models.Exercise).all()
    return exercises


async def get_exercise(exercise_id, database) -> models.Exercise:
    exercise = database.query(models.Exercise).get(exercise_id)
    return exercise


async def get_all_workout_exercises(workout_id, database) -> List[models.Exercise]:
    exercises = database.query(WorkoutExercise).filter(WorkoutExercise.workout_id == workout_id)
    exercise_list = list()
    for x in exercises:
        exercise_id = x.exercise_id
        exercise_list.append(database.query(models.Exercise).get(exercise_id))

    return exercise_list


# async def get_all_users_exercises(user_id, database) -> List[models.Exercise]:
#     exercises = database.query


# async def update_exercise(request, database) -> models.Exercise:
#     old_exercise = database.query(models.Exercise).get(request.id)
#     if not old_exercise:
#         raise status.HTTP_404_NOT_FOUND
#     request_data = request.dict(exclude_unset=True)
# try and do a delete, and create a new exercise???


async def delete_exercise_from_workout(request, database):
    database.query(WorkoutExercise).filter(WorkoutExercise.workout_id == request.workout_id,
                                           WorkoutExercise.exercise_id == request.exercise_id).delete()
    database.commit()


async def delete_exercise(exercise_id, database):
    database.query(models.Exercise).filter(models.Exercise.id == exercise_id).delete()
    database.commit()
