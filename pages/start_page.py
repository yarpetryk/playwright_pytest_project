from playwright.sync_api import Page
from helpers.constants import WebPageUrl
import allure


class StartPage():

    def __init__(self, page: Page) -> None:
        self.page = page
        self.username_input = page.locator('#Username')
        self.password_input = page.locator('#Password')
        self.login_button = page.locator('//*[contains(@type, "submit")]')
        self.logout_button = page.get_by_role("link", name="Abmelden")
        self.devices_link = page.get_by_role("link", name="Boxen")


    @allure.step('And load page')
    def load(self, url) -> None:
        self.page.goto(url)
        self.page.wait_for_load_state('networkidle')

    @allure.step('And login to account')
    def login(self, login, password) -> None:
        self.username_input.fill(login)
        # self.username_input.press('Tab')
        self.password_input.fill(password)
        self.login_button.click()


    @allure.step('And proceed to Devices page')
    def proceed_to_devices_tab(self) -> None:
        self.devices_link.click()
        self.page.wait_for_url(WebPageUrl.DEVICES_PAGE)


