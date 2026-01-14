from sqlmodel import create_engine
from sqlalchemy import text

from .settings import get_settings

settings = get_settings()
engine = create_engine(settings.database_url, echo=True)

def test_db_connection() -> None:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
        
def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
        