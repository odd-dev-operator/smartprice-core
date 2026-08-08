from app.models.price_result import PriceResult
from app.models.product import Product
from app.scrapers.base import BaseScraper
from app.stores.store import Store


class MockScraper(BaseScraper):

    def __init__(self, store: Store, price: float):
        self.store = store
        self.price = price

    def search(self, product: Product) -> list[PriceResult]:
        return [
            PriceResult(
                product=product,
                store=self.store,
                price=self.price,
                currency="EUR",
                url=self.store.website,
            )
        ]