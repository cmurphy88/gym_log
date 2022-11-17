from pydantic import BaseModel


class Exercise(BaseModel):
    name: str


class DisplayExercise(BaseModel):
    id: int
    name: str
