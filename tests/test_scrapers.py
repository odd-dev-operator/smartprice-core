import pytest

from app.scrapers.base import BaseScraper


def test_base_scraper_cannot_be_instantiated():
    with pytest.raises(TypeError):
        BaseScraper()