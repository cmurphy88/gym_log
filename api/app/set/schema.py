from datetime import datetime
from sqlite3 import Date
from typing import Optional
from pydantic import BaseModel


class Set(BaseModel):
    weight: float
    reps: int
    exercise_id: int
    date: Date


class DisplaySet(BaseModel):
    id: int
    weight: float
    reps: int
    exercise_id: int
    date: Date

    class Config:
        orm_mode = True
