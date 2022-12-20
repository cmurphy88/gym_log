from typing import Optional

from sqlalchemy.orm import Session

from . models import Workout


async def verify_workout_exist(name: str, user_id: int, db_session: Session) -> Optional[Workout]:
    workout = db_session.query(Workout).filter(Workout.user_id == user_id, Workout.name == name).all()
    if workout:
        return workout
