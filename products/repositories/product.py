from sqlalchemy.orm import Session
from .. import  models,schemas
from fastapi import  Response,status,HTTPException


def get_all(db :Session):
    products=db.query(models.Products).all()
    return {"success":"true","message":"","data":products}

def create(request: schemas.Products,db : Session):
    new_product= models.Products(name=request.name, price=request.price, imgUrl=request.imgUrl, quantity=request.quantity, category_id=2)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return {"success":"true","message":"product created successfully","data":request}

def show(id, db : Session):
    product=db.query(models.Products).where(models.Products.id==id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"product with id {id} does not exist")
    return product

def get_by_category(cat_id, db : Session):
    product=db.query(models.Products).all()
    filteredProducts = []
    for p in product:
        if int(p.category_id) == int(cat_id):
            filteredProducts.append(p)
    if not filteredProducts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"product with category id {cat_id} does not exist")
    return {"success":"true","message":"","data":filteredProducts}

def update(id, request: schemas.Products, db : Session):
    product = db.query(models.Products).filter(models.Products.id == id)
    if not product.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"product with id {id} not found")

    product.update(request.dict())
    db.commit()
    return {"success":"true","message":"product updated successfully"}