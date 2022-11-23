from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Set(BaseModel):
    weight: float
    reps: int
    exercise_id: int
    date: datetime


class DisplaySet(BaseModel):
    id: int
    weight: float
    reps: int
    exercise_id: int
    date: datetime

    class Config:
        orm_mode = True
