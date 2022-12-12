from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from .. import db
from . import schema
from . import services

router = APIRouter(tags=['Session'], prefix='/sessions')


@router.post('/new', status_code=status.HTTP_201_CREATED)
async def create_new_session(request: schema.Session, database: Session = Depends(db.get_db)):
    return await services.create_new_session(request, database)


@router.get('/all', response_model=List[schema.Session])
async def get_all_sessions(database: Session = Depends(db.get_db)):
    return await services.get_all_sessions(database)
