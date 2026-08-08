from dataclasses import dataclass

from app.models.product import Product
from app.stores.store import Store


@dataclass
class PriceResult:
    product: Product
    store: Store
    price: float
    currency: str
    url: str