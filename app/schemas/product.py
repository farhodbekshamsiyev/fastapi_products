from typing import Optional
from pydantic import BaseModel, Field, field_validator


class ProductBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=32)
    price: int = Field(..., ge=0)
    quantity: int = Field(..., ge=0)
    catalog_id: Optional[int] = None

    @field_validator('name')
    def name_cannot_be_null(cls, v):
        if v is None or not v.strip():
            raise ValueError('Product name cannot be null or empty')
        return v


class ProductCreate(ProductBase):
    pass


class ProductOut(ProductBase):
    id: int

    class Config:
        from_attributes = True
