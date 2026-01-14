from fastapi import FastAPI, Depends
from sqlmodel import Session

from .database import test_db_connection, create_db_and_tables, get_session
from . import models

app = FastAPI()

@app.on_event("startup")
def on_startup():
    test_db_connection()

@app.get("/")    
def root():
    return {"message": "FastAPI is running"}

@app.get("/health/db")
def health_db():
    return {"status": "ok"}