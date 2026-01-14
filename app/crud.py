from sqlmodel import Session

from .models import Item, ItemCreate

def create_item(session: Session, item_create: ItemCreate) -> Item:
    item = Item.model_validate(item_create)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item