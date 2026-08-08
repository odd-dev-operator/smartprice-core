from app.models.category import Category
from app.models.product import Product
from app.scrapers.mock import MockScraper
from app.services.store_manager import StoreManager
from app.stores.store import Store


def test_store_manager_combines_results_from_multiple_scrapers():
    product = Product(
        name="LG OLED C5 65\"",
        category=Category.TELEVISIONS,
        brand="LG",
        model="OLED65C5",
    )

    store_a = Store(
        name="Store A",
        country="PT",
        website="https://example-a.com",
    )

    store_b = Store(
        name="Store B",
        country="ES",
        website="https://example-b.com",
    )

    scraper_a = MockScraper(
        store=store_a,
        price=1349.99,
    )

    scraper_b = MockScraper(
        store=store_b,
        price=1299.99,
    )

    manager = StoreManager([scraper_a, scraper_b])

    results = manager.search(product)

    assert len(results) == 2
    assert results[0].store == store_a
    assert results[0].price == 1349.99
    assert results[1].store == store_b
    assert results[1].price == 1299.99