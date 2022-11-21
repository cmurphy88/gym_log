from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..db import Base


class Workout(Base):
    __tablename__ = "workout"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    user_id = Column(Integer)

    def __init__(self, name, user_id, *args, **kwargs):
        self.name = name
        self.user_id = user_id


class WorkoutExercise(Base):
    __tablename__ = "workout_exercise"

    id = Column(Integer, primary_key=True, autoincrement=True)
    workout_id = Column(Integer)
    exercise_id = Column(Integer)

    def __init__(self, name, workout_id, exercise_id, *args, **kwargs):
        self.name = name
        self.workout_id = workout_id
        self.exercise_id = exercise_id
