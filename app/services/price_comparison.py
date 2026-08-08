from app.models.price_result import PriceResult


def find_best_price(results: list[PriceResult]) -> PriceResult | None:
    if not results:
        return None

    return min(results, key=lambda result: result.price)