from pydantic import BaseModel, Field, field_validator


class CatalogBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=32)

    @field_validator('name')
    def name_cannot_be_null(cls, v):
        if v is None or not v.strip():
            raise ValueError('Catalog name cannot be null or empty')
        return v


class CatalogCreate(CatalogBase):
    pass


class CatalogOut(CatalogBase):
    id: int

    class Config:
        from_attributes = True
