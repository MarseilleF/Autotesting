from playwright.sync_api import expect
class BasePage:
    MAIN_PAGE = 'https://the-internet.herokuapp.com/'
    def __init__(self, page):
        self.page = page
    def find(self, *args):
        return self.page.locator(args)
    def open(self, url):
        return self.page.goto(url)
    def check_url(self, url):
        return expect(self.page).to_have_url(url)