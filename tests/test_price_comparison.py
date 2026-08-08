from app.models.category import Category
from app.models.product import Product
from app.models.price_result import PriceResult
from app.services.price_comparison import find_best_price
from app.stores.store import Store


def test_find_best_price():
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

    result_a = PriceResult(
        product=product,
        store=store_a,
        price=1349.99,
        currency="EUR",
        url="https://example-a.com/product",
    )

    result_b = PriceResult(
        product=product,
        store=store_b,
        price=1299.99,
        currency="EUR",
        url="https://example-b.com/product",
    )

    best = find_best_price([result_a, result_b])

    assert best == result_b


def test_find_best_price_with_no_results():
    assert find_best_price([]) is None