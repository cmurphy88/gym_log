from datetime import datetime
from sqlite3 import Date
from typing import Optional
from pydantic import BaseModel


class Session(BaseModel):
    date: Date


class DisplaySession(BaseModel):
    id: int
    date: Date

    class Config:
        orm_mode = True
