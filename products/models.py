from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer,primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)
    imgUrl = Column(String)
    quantity = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="products")


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer,primary_key=True, index=True)
    name = Column(String)
    products = relationship('Products', back_populates="category")
