from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..db import Base


class Exercise(Base):
    __tablename__ = "exercise"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))

    def __init__(self, name, *args, **kwargs):
        self.name = name
