from abc import ABC, abstractmethod
from typing import Any

class ProductRepository(ABC):
    @abstractmethod
    def create(self, data: dict) -> Any:
        pass

    @abstractmethod
    def list_all(self) -> list[dict]:
        pass

    @abstractmethod
    def get(self, product_id: Any) -> Any:
        pass

    @abstractmethod
    def update(self, product_id: Any, data: dict) -> Any:
        pass

    @abstractmethod
    def delete(self, product_id: Any) -> bool:
        pass

    @abstractmethod
    def get_products_by_catalog(self, catalog_id: Any) -> list[dict]:
        pass

    @abstractmethod
    def assign_product_to_catalog(self, product_id: Any, catalog_id: Any) -> Any:
        pass
