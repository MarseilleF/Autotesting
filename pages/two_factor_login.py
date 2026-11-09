from pages.base_page import BasePage
import pytest
from playwright.sync_api import expect

class TwoFactor(BasePage):
    LOGIN_PAGE = 'https://the-internet.herokuapp.com/two_factor'
    def __init__(self, page):
        super().__init__(page)
        self.TWO_FACTOR_PAGE = 'https://the-internet.herokuapp.com/two_factor/code'
        self.TWO_FACTOR_CODE = page.locator('strong[id=otp-code]')
        self.USERNAME_INPUT = page.locator('input[name="username"]')
        self.PASSWORD_INPUT = page.locator('input[name="password"]')
        self.BUTTON_LOGIN = page.locator('button[class="radius"]')
        self.TWO_FACTOR_INPUT = page.locator('input[id="code"]')
    def open_page(self):
        return super().open(self.LOGIN_PAGE)
    def check_registration_form_visibility(self):
        expect(self.USERNAME_INPUT).to_be_visible()
        expect(self.PASSWORD_INPUT).to_be_visible()
        expect(self.BUTTON_LOGIN).to_be_visible()
    def fill_registration_form(self, test_data):
        self.USERNAME_INPUT.fill(test_data['login'])
        self.PASSWORD_INPUT.fill(test_data['password'])
    def click_login(self):
        self.BUTTON_LOGIN.click()
    def check_opened(self):
        return super().check_url(self.TWO_FACTOR_PAGE)
    def fill_otp(self):
         self.TWO_FACTOR_INPUT.fill(self.TWO_FACTOR_CODE.text_content())
         self.BUTTON_LOGIN.click()



