from app.scrapers.base import BaseScraper
from app.stores.store import Store


class StoreRegistry:
    def __init__(self) -> None:
        self._entries: list[tuple[Store, BaseScraper]] = []

    def register(self, store: Store, scraper: BaseScraper) -> None:
        self._entries.append((store, scraper))

    def get_active(self) -> list[tuple[Store, BaseScraper]]:
        return [
            (store, scraper)
            for store, scraper in self._entries
            if store.active
        ]