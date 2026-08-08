from app.models.category import Category
from app.models.product import Product
from app.services.product_matching import products_match


def test_products_match_when_ean_is_equal():
    product_a = Product(
        name='LG OLED C5 65"',
        category=Category.TELEVISIONS,
        brand="LG",
        model="OLED65C54LA",
        ean="8806096362426",
    )

    product_b = Product(
        name="LG OLED 65 C5",
        category=Category.TELEVISIONS,
        brand="LG",
        model="OLED65C54LA",
        ean="8806096362426",
    )

    assert products_match(product_a, product_b)


def test_products_do_not_match_when_ean_is_different():
    product_a = Product(
        name='LG OLED C5 65"',
        category=Category.TELEVISIONS,
        brand="LG",
        model="OLED65C54LA",
        ean="8806096362426",
    )

    product_b = Product(
        name="LG OLED 65 C5",
        category=Category.TELEVISIONS,
        brand="LG",
        model="OLED65C54LA",
        ean="8806096362427",
    )

    assert not products_match(product_a, product_b)


def test_products_do_not_match_when_ean_is_missing():
    product_a = Product(
        name='LG OLED C5 65"',
        category=Category.TELEVISIONS,
        brand="LG",
        model="OLED65C54LA",
        ean="8806096362426",
    )

    product_b = Product(
        name="LG OLED 65 C5",
        category=Category.TELEVISIONS,
        brand="LG",
        model="OLED65C54LA",
    )

    assert not products_match(product_a, product_b)