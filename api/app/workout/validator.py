# from typing import Optional
#
# from sqlalchemy.orm import Session
#
# from . models import Workout
#
#
# async def verify_workout_exist(name: str, user_id: int, db_session: Session) -> Optional[Workout]:
#     workouts = db_session.query(Workout).filter(Workout.user_id == user_id).first()
#     for x in workouts:
#         if x.name == name:
#             return x
