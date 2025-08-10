from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class Catalog(BaseModel):
    __tablename__ = "catalogs"

    name = Column(String, unique=True, index=True, nullable=False)
    products = relationship("Product", back_populates="catalog")

    def __repr__(self):
        return f"<Catalog(id={self.id}, name='{self.name}')>"
