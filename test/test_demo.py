import time
import pytest
from playwright.sync_api import expect, Page
from pages.secure_area import Secure_Area
from pages.two_factor_login import TwoFactor



@pytest.mark.ui
def test_successful_login(
                          before_after,
                          page: Page,
                          test_data: dict,
                          secure_area: Secure_Area,
                          two_factor: TwoFactor
                          ):
        two_factor.open_page()
        two_factor.check_registration_form_visibility()
        two_factor.fill_registration_form(test_data)
        two_factor.click_login()
        two_factor.check_opened()
        two_factor.fill_otp()
        secure_area.check_opened()
        secure_area.check_visible_title()
# def test_demo2(before_after):
#     assert 1 == 1
# def test_demo(before_after):
#     assert 3 == 2
