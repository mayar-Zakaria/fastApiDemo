from fastapi import FastAPI
from .database import engine
from . import models
from sqlalchemy.orm import Session
from .routers import product, category
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(engine)

app.include_router(product.router)
app.include_router(category.router)


