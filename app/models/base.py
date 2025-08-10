from sqlalchemy import Column, Integer, DateTime, func
from app.database import Base

class BaseModel(Base):
    """
    Abstract base model with id, created_at, and updated_at fields.
    """
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
