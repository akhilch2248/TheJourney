from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    provider: str
    provider_id: str
    email: Optional[str]

class UserRead(BaseModel):
    id: int
    provider: str
    provider_id: str
    email: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True

