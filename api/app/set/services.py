from typing import List, Optional
from fastapi import HTTPException, status
from . import models


async def create_new_set(request, database) -> models.Set:
    new_set = models.set(name=request.name, user_id=request.user_id)
    database.add(new_set)
    database.commit()
    database.refresh(new_set)
    return new_set


async def get_all_sets(database) -> List[models.Set]:
    sets = database.query(models.Set).all()
    return sets


async def get_set_by_id(set_id, database) -> models.Set:
    set = database.query(models.Set).get(set_id)
    return set


async def delete_set(set_id, database):
    database.query(models.Set).filter(models.Set.id == set_id).delete()
    database.commit()
