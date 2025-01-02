import pytest

from playwright.sync_api import Page, expect
from helpers.constants import UserCredentials, WebPageUrl
from pages.start_page import StartPage
from pages.devices_page import DevicesPage


@pytest.fixture
def start_page(page: Page) -> StartPage:
    return StartPage(page)

@pytest.fixture
def devices_page(page: Page) -> DevicesPage:
    return DevicesPage(page)

@pytest.fixture()
# def login_set_up(page: Page, url: str) -> None:
def login_set_up(page: Page) -> Page:
    username_input = page.locator('#Username')
    password_input = page.locator('#Password')
    login_button = page.locator('//*[contains(@type, "submit")]')
    logout_button = page.get_by_role("link", name="Abmelden")
    page.goto(WebPageUrl.START_PAGE)
    page.wait_for_load_state('networkidle')
    username_input.fill(UserCredentials.USERNAME)
    password_input.fill(UserCredentials.PASSWORD)
    login_button.click()
    expect(logout_button).to_be_visible()
    yield page
    page.close()
