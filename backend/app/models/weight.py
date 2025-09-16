from sqlalchemy import Column, Integer, Float, String, Date, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class WeightLog(Base):
    __tablename__ = "weights"

    id = Column(Integer, primary_key=True, index=True)  # Unique ID
    date = Column(Date, nullable=False)                # Date of log
    weight_kg = Column(Float, nullable=False)          # Weight in kg
    source = Column(String, default="manual")          # Source: manual, apple_health, renpho

# New fields
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


# ✅ NEW: tie each log to a user
    user_id = Column(Integer, ForeignKey("users.id"))

    # Relationship (optional for ORM usage)
    user = relationship("User", back_populates="weights")
