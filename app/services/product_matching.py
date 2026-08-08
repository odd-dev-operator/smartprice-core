from app.models.product import Product


def products_match(product_a: Product, product_b: Product) -> bool:
    if not product_a.ean or not product_b.ean:
        return False

    return product_a.ean == product_b.ean