from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, DATE
from sqlalchemy.orm import relationship
from ..db import Base


class Set(Base):
    __tablename__ = "set"

    id = Column(Integer, primary_key=True, autoincrement=True)
    weight = Column(DECIMAL)
    reps = Column(Integer)
    exercise_id = Column(Integer, ForeignKey("exercise.id"))

    def __init__(self, weight, reps, exercise_id, *args, **kwargs):
        self.weight = weight
        self.reps = reps
        self.exercise_id = exercise_id
