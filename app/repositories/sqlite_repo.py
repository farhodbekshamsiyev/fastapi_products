from sqlalchemy.orm import Session
from app.models.product import Product
from app.database import SessionLocal
from app.repositories.base_repo import ProductRepository

class SQLiteProductRepository(ProductRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: dict):
        product = Product(**data)
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def list_all(self):
        return self.db.query(Product).all()

    def get(self, product_id: int):
        return self.db.query(Product).filter(Product.id == product_id).first()

    def update(self, product_id: int, data: dict):
        product = self.get(product_id)
        if not product:
            return None
        for key, value in data.items():
            setattr(product, key, value)
        self.db.commit()
        self.db.refresh(product)
        return product

    def delete(self, product_id: int):
        product = self.get(product_id)
        if not product:
            return False
        self.db.delete(product)
        self.db.commit()
        return True

    def get_products_by_catalog(self, catalog_id: int):
        return self.db.query(Product).filter(Product.catalog_id == catalog_id).all()

    def assign_product_to_catalog(self, product_id: int, catalog_id: int):
        product = self.get(product_id)
        if not product:
            return None
        product.catalog_id = catalog_id
        self.db.commit()
        self.db.refresh(product)
        return product

def get_sqlite_repo():
    db = SessionLocal()
    try:
        yield SQLiteProductRepository(db)
    finally:
        db.close()
