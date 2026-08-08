from dataclasses import dataclass

from app.models.category import Category


@dataclass
class Product:
    name: str
    category: Category
    brand: str | None = None
    model: str | None = None