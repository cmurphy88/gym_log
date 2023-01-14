from sqlite3 import Date
from pydantic import BaseModel


class Set(BaseModel):
    weight: float
    reps: int
    exercise_id: int


class DisplaySet(BaseModel):
    id: int
    weight: float
    reps: int
    exercise_id: int

    class Config:
        orm_mode = True


class SetDate(BaseModel):
    date: Date

    class Config:
        orm_mode = True
