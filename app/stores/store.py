from dataclasses import dataclass


@dataclass
class Store:
    name: str
    country: str
    website: str
    active: bool = True

    def __post_init__(self) -> None:
        self.country = self.country.upper()

        if len(self.country) != 2 or not self.country.isalpha():
            raise ValueError(
                "country must be a 2-letter ISO country code"
            )