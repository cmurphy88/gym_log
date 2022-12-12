from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, DATE
# from sqlalchemy.orm import relationship
from ..db import Base


class Session(Base):
    __tablename__ = "session"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DATE)

    def __init__(self, date, *args, **kwargs):
        self.date = date
