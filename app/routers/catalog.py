from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.catalog import Catalog
from app.schemas.catalog import CatalogCreate, CatalogOut

router = APIRouter(prefix="/catalogs", tags=["catalogs"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=CatalogOut)
def create_catalog(catalog: CatalogCreate, db: Session = Depends(get_db)):
    db_catalog = Catalog(name=catalog.name)
    db.add(db_catalog)
    db.commit()
    db.refresh(db_catalog)
    return db_catalog


@router.get("/", response_model=list[CatalogOut])
def get_catalogs(db: Session = Depends(get_db)):
    return db.query(Catalog).all()


@router.put("/{catalog_id}", response_model=CatalogOut)
def update_catalog(catalog_id: int, catalog: CatalogCreate, db: Session = Depends(get_db)):
    db_catalog = db.query(Catalog).filter(Catalog.id == catalog_id).first()
    if not db_catalog:
        raise HTTPException(status_code=404, detail="Catalog not found")
    db_catalog.name = catalog.name
    db.commit()
    db.refresh(db_catalog)
    return db_catalog


@router.delete("/{catalog_id}", status_code=204)
def delete_catalog(catalog_id: int, db: Session = Depends(get_db)):
    db_catalog = db.query(Catalog).filter(Catalog.id == catalog_id).first()
    if not db_catalog:
        raise HTTPException(status_code=404, detail="Catalog not found")
    db.delete(db_catalog)
    db.commit()
    return None
