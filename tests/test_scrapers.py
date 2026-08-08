from app.models.category import Category
from app.models.product import Product
from app.scrapers.base import BaseScraper
from app.scrapers.mock import MockScraper
from app.stores.store import Store


def test_base_scraper_cannot_be_instantiated():
    try:
        BaseScraper()
        assert False
    except TypeError:
        pass


def test_mock_scraper_returns_price_result():
    product = Product(
        name="LG OLED C5 65\"",
        category=Category.TELEVISIONS,
        brand="LG",
        model="OLED65C5",
    )

    store = Store(
        name="Mock Store",
        country="PT",
        website="https://example.com",
    )

    scraper = MockScraper(
        store=store,
        price=1299.99,
    )

    results = scraper.search(product)

    assert len(results) == 1
    assert results[0].product == product
    assert results[0].store == store
    assert results[0].price == 1299.99
    assert results[0].currency == "EUR"
    assert results[0].url == "https://example.com"