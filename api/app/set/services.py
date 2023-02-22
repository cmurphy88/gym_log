from typing import List
from . import models
from ..workout.models import WorkoutExercise
from .schema import SetWithDate
from ..session.models import Session


async def create_new_set(request, database) -> models.Set:
    new_set = models.set(name=request.name, user_id=request.user_id)
    database.add(new_set)
    database.commit()
    database.refresh(new_set)
    return new_set


async def get_all_sets(database) -> List[models.Set]:
    sets = database.query(models.Set).all()
    return sets


async def get_set_by_id(set_id, database) -> models.Set:
    set = database.query(models.Set).get(set_id)
    return set


async def get_all_exercise_sets(exercise_id, database) -> List[models.Set]:
    sets = database.query(models.Set).filter(models.Set.exercise_id == exercise_id)
    sets_list = list()
    for x in sets:
        sets_list.append(x)
    return sets_list


async def get_all_workout_sets(workout_id, database) -> List[models.Set]:
    exercises = database.query(WorkoutExercise).filter(WorkoutExercise.workout_id == workout_id)
    exercise_list = list()
    sets_list = list()
    for x in exercises:
        exercise_id = x.exercise_id
        exercise_list.append(database.query(models.Set).get(exercise_id))

    for x in exercise_list:
        exercise_id = x.exercise_id
        sets = database.query(models.Set).filter(models.Set.exercise_id == exercise_id)

        for y in sets:
            sets_list.append(y)
    return sets_list


async def get_set_date(exercise_id, database) -> List[SetWithDate]:
    sets_list = list()
    sets_date_list = list()
    session_list = list()
    sets = database.query(models.Set).filter(models.Set.exercise_id == exercise_id)
    for x in sets:
        sets_list.append(x)

    for x in sets_list:
        session = database.query(Session).filter(Session.id == int(x.session_id))
        for y in session:
            session_list.append(y)
        date = session_list[0].date
        set_with_date = SetWithDate(
            weight=x.weight,
            reps=x.weight,
            date=date
        )
        sets_date_list.append(set_with_date)

    return sets_date_list


async def delete_set(set_id, database):
    database.query(models.Set).filter(models.Set.id == set_id).delete()
    database.commit()
