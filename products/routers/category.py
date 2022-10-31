from fastapi import APIRouter,Depends, Response,status,HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..repositories import category

router = APIRouter(
    prefix="/categories",
    tags=['categories']
)

@router.post("", tags=['categories'])
def create_category(request: schemas.Category, db: Session = Depends(database.get_db)):
    return category.create(request, db)

@router.get("", tags=['categories'])   
def all_categories(db :Session = Depends(database.get_db)):
    return category.get_all(db)