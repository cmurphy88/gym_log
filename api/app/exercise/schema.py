from typing import Optional

from pydantic import BaseModel


class Exercise(BaseModel):
    name: str


class DisplayExercise(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class UpdateExercise(BaseModel):
    id: Optional[int]
    name: Optional[str]

    class Config:
        orm_mode: True
