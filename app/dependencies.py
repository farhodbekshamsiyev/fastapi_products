import os
from fastapi import Depends
from app.repositories.sqlite_repo import get_sqlite_repo
from app.repositories.mongo_repo import get_mongo_repo
from app.repositories.base_repo import ProductRepository

def get_product_repository(repo: str = os.getenv("DB_BACKEND", "sqlite")) -> ProductRepository:
    if repo == "mongo":
        return next(get_mongo_repo())
    return next(get_sqlite_repo())
