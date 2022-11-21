from typing import Optional
from pydantic import BaseModel


class Workout(BaseModel):
    name: str
    user_id: int


class DisplayWorkout(BaseModel):
    id: int
    name: str
    user_id: int

    class Config:
        orm_mode = True
