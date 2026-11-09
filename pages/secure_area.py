from pages.base_page import BasePage
from playwright.sync_api import expect
class Secure_Area(BasePage):
    URL = "https://the-internet.herokuapp.com/two_factor/secure"
    def __init__(self, page):
        super().__init__(page)
        self.TITLE = page.locator("//h2")
        self.TITLE_TEXT = "Secure Area"
    def check_visible_title(self):
        expect(self.TITLE).to_be_visible()
        expect(self.TITLE).to_have_text(self.TITLE_TEXT)
    def check_opened(self):
        return super().check_url(self.URL)