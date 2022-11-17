from typing import List, Optional
from fastapi import HTTPException, status
from . import models


async def get_all_exercises(database) -> List[models.Exercise]:
    exercises = database.query(models.Exercise).all()
    if exercises:
        return exercises
    else:
        return "null"
