from app.models.category import Category
from app.models.price_result import PriceResult
from app.models.product import Product
from app.stores.store import Store


def test_category_audio():
    assert Category.AUDIO.value == "audio"


def test_product_creation():
    product = Product(
        name="LG OLED C5 65\"",
        category=Category.TELEVISIONS,
        brand="LG",
        model="OLED65C5",
    )

    assert product.name == "LG OLED C5 65\""
    assert product.category == Category.TELEVISIONS
    assert product.brand == "LG"
    assert product.model == "OLED65C5"


def test_store_creation():
    store = Store(
        name="Amazon ES",
        country="ES",
        website="https://www.amazon.es",
    )

    assert store.name == "Amazon ES"
    assert store.country == "ES"
    assert store.website == "https://www.amazon.es"


def test_price_result_creation():
    product = Product(
        name="LG OLED C5 65\"",
        category=Category.TELEVISIONS,
        brand="LG",
        model="OLED65C5",
    )

    store = Store(
        name="Amazon ES",
        country="ES",
        website="https://www.amazon.es",
    )

    result = PriceResult(
        product=product,
        store=store,
        price=1299.99,
        currency="EUR",
        url="https://www.amazon.es",
    )

    assert result.product == product
    assert result.store == store
    assert result.price == 1299.99
    assert result.currency == "EUR"
    assert result.url == "https://www.amazon.es"