from typing import List, Optional
from fastapi import HTTPException, status
from . import models


async def create_new_session(request, database) -> models.Session:
    new_session = models.Session(date=request.date)
    database.add(new_session)
    database.commit()
    database.refresh(new_session)
    return new_session
