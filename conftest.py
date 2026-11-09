import pytest
from playwright.sync_api import Page
from pages.two_factor_login import  TwoFactor
from pages.secure_area import Secure_Area

@pytest.fixture
def test_data():
        return {
                "login": "tomsmith",
                "password": "SuperSecretPassword!"
        }
@pytest.fixture
def before_after():
    print("\n__________")
    yield
    print("\n__________")
@pytest.fixture
def two_factor(page: Page):
    return TwoFactor(page)
@pytest.fixture
def secure_area(page: Page):
    return Secure_Area(page)