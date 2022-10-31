from fastapi import APIRouter,Depends, Response,status,HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..repositories import product
router = APIRouter(
    prefix="/products",
    tags=['products']
)

@router.post('', status_code=status.HTTP_201_CREATED )
def create(request: schemas.Products, db:Session = Depends(database.get_db)):
    return product.create(request, db)

@router.get("/categoryID={id}",status_code=200)
def get_by_category(id, response:Response, db :Session = Depends(database.get_db)):
    print("category")
    return product.get_by_category(id,db)

@router.get("", tags=['products'])   
def all(db :Session = Depends(database.get_db), tags=['products']):
    print("get all")
    return product.get_all(db)

@router.get("/{id}",status_code=200,  response_model=schemas.showProduct)
def show(id, response:Response, db :Session = Depends(database.get_db)):
    return product.show(id,db)


@router.put("/{id}" ,status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Products, db: Session = Depends(database.get_db)):
    return product.update(id,request,db)