from pydantic import BaseModel


class Products(BaseModel):
    name: str
    price: int
    imgUrl: str
    quantity: int

class Category(BaseModel):
    name: str
    class Config:
        orm_mode = True

class showProduct(BaseModel):
    name: str
    price: int
    imgUrl: str
    quantity: int
    category: Category
    class Config():
        orm_mode = True

