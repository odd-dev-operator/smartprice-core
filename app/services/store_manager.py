from app.models.price_result import PriceResult
from app.models.product import Product
from app.scrapers.base import BaseScraper


class StoreManager:
    def __init__(self, scrapers: list[BaseScraper]):
        self.scrapers = scrapers

    def search(self, product: Product) -> list[PriceResult]:
        results: list[PriceResult] = []

        for scraper in self.scrapers:
            results.extend(scraper.search(product))

        return results