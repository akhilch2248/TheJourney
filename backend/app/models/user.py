from sqlalchemy import Column, Integer, String, DateTime, func
from ..database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    provider = Column(String, nullable=False)   # "apple" or "google"
    provider_id = Column(String, unique=True, nullable=False)  # Unique ID from Apple/Google
    email = Column(String, unique=True, nullable=True)  # Sometimes available
    created_at = Column(DateTime(timezone=True), server_default=func.now())

# ✅ NEW: one-to-many link to weights
    weights = relationship("WeightLog", back_populates="user")
