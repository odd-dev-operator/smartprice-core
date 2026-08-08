from abc import ABC, abstractmethod

from app.models.price_result import PriceResult
from app.models.product import Product


class BaseScraper(ABC):

    @abstractmethod
    def search(self, product: Product) -> list[PriceResult]:
        """Search for a product and return the available prices."""
        raise NotImplementedError