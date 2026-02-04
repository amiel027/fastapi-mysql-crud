from fastapi import FastAPI, Depends
from sqlmodel import Session

from .database import test_db_connection, create_db_and_tables, get_session
from . import models
from .models import ItemCreate, ItemRead
from .crud import create_item, get_item, list_items

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

@app.get("/items", response_model=list[ItemRead])
def list_items_rout(limit: int = 100,session: Session = Depends(get_session)):
    return list_items(session, limit=limit)

@app.get("/items/{item_id}", response_model=ItemRead)
def get_item_route(item_id: int, session: Session = Depends(get_session)):
    item = get_item(session, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item