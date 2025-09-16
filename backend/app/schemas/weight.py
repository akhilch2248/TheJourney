from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import Optional

class WeightCreate(BaseModel):
    date: date
    weight_kg: float = Field(gt=0, description="Weight must be greater than 0")
    source: Optional[str] = "manual"

class WeightRead(BaseModel):
    id: int
    date: date
    weight_kg: float
    source: str
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True

