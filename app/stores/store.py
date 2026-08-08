from dataclasses import dataclass


@dataclass
class Store:
    name: str
    country: str
    website: str