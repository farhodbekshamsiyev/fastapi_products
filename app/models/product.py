from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class Product(BaseModel):
    __tablename__ = "products"

    name = Column(String, index=True, nullable=False)
    price = Column(Integer, nullable=False, default=0)
    quantity = Column(Integer, nullable=False, default=0)
    catalog_id = Column(Integer, ForeignKey("catalogs.id"), nullable=True)

    catalog = relationship("Catalog", back_populates="products")

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', catalog_id={self.catalog_id})>"
