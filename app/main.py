from fastapi import FastAPI, Depends
from sqlmodel import Session

from .database import test_db_connection, create_db_and_tables, get_session
from . import models
from .models import ItemCreate, ItemRead
from .crud import create_item

app = FastAPI()

@app.on_event("startup")
def on_startup():
    test_db_connection()
    create_db_and_tables()

@app.get("/")    
def root():
    return {"message": "FastAPI is running"}

@app.get("/health/db")
def health_db(session: Session = Depends(get_session)):
    return {"status": "ok"}

@app.post("/items", response_model=ItemRead, status_code=201)
def create_item_route(item: ItemCreate, session: Session = Depends(get_session)):
    created = create_item(session, item)
    return created