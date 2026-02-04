from typing import List, Optional
from sqlmodel import Session, select

from .models import Item, ItemCreate

def create_item(session: Session, item_create: ItemCreate) -> Item:
    item = Item.model_validate(item_create)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

def get_item(session: Session, item_id: int) -> Optional[Item]:
    return session.get(Item, item_id)

def list_items(session: Session, limit: int = 100) -> List[Item]:
    statement = select(Item).limit(limit)
    results = session.exec(statement)
    return results.all()