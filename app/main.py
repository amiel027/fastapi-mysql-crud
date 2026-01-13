from fastapi import FastAPI
from .database import test_db_connection

app = FastAPI()

@app.on_event("startup")
def on_startup():
    test_db_connection()

@app.get("/")    
def root():
    return {"message": "FastAPI is running"}