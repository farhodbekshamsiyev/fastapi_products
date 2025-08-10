from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.dependencies import get_product_repository
from app.models.product import Product
from app.repositories.base_repo import ProductRepository
from app.schemas.product import ProductCreate, ProductOut

router = APIRouter(prefix="/products", tags=["products"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ProductOut)
def create_product(product: ProductCreate, repo: ProductRepository = Depends(get_product_repository)):
    return repo.create(product.model_dump())


@router.get("/", response_model=list[ProductOut])
def get_products(repo: ProductRepository = Depends(get_product_repository)):
    return repo.list_all()


@router.get("/{product_id}", response_model=ProductOut)
def get_product(product_id: int, repo: ProductRepository = Depends(get_product_repository)):
    product = repo.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.put("/{product_id}", response_model=ProductOut)
def update_product(product_id: int, product: ProductCreate, repo: ProductRepository = Depends(get_product_repository)):
    updated = repo.update(product_id, product.model_dump())
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated


@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: int, repo: ProductRepository = Depends(get_product_repository)):
    deleted = repo.delete(product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return None


@router.get("/by-catalog/{catalog_id}", response_model=list[ProductOut])
def get_products_by_catalog(catalog_id: int, repo: ProductRepository = Depends(get_product_repository)):
    return repo.get_products_by_catalog(catalog_id)


@router.patch("/{product_id}/add-to-catalog", response_model=ProductOut)
def assign_product_to_catalog(product_id: int, catalog_id: int = Body(..., embed=True), repo: ProductRepository = Depends(get_product_repository)):
    updated = repo.assign_product_to_catalog(product_id, catalog_id)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated
