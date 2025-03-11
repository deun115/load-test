import datetime
from pydantic import BaseModel

class UserCreate(BaseModel):
    user_id: int 
    item_id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
