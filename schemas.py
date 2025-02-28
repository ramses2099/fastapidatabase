from typing import Optional
from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None
    
class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    user_id: int
    
    class Config:
        from_attributes = True
        
class UserBase(BaseModel):
    email: str
    
class UserCreate(BaseModel):
    password: str
    
class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []
    
    class Config:
        from_attributes = True
        