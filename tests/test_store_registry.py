from app.models.category import Category
from app.models.product import Product
from app.scrapers.mock import MockScraper
from app.services.store_registry import StoreRegistry
from app.stores.store import Store


def test_registry_returns_active_stores():
    store_a = Store(
        name="Store A",
        country="PT",
        website="https://example-a.com",
    )

    store_b = Store(
        name="Store B",
        country="ES",
        website="https://example-b.com",
        active=False,
    )

    product = Product(
        name="LG OLED C5 65\"",
        category=Category.TELEVISIONS,
        brand="LG",
        model="OLED65C5",
    )

    scraper_a = MockScraper(store=store_a, price=1349.99)
    scraper_b = MockScraper(store=store_b, price=1299.99)

    registry = StoreRegistry()

    registry.register(store_a, scraper_a)
    registry.register(store_b, scraper_b)

    active = registry.get_active()

    assert len(active) == 1
    assert active[0][0] == store_a
    assert active[0][1] == scraper_a