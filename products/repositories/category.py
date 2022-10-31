from sqlalchemy.orm import Session
from .. import  models,schemas
from fastapi import  Response,status,HTTPException

def get_all(db :Session):
    categories=db.query(models.Category).all()
    return {"success":"true","message":"","data":categories}

def create(request: schemas.Category, db: Session):
    new_category= models.Category(name=request.name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return {"success":"true","message":"category created successfully","data":request}