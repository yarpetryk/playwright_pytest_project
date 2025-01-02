from playwright.sync_api import Page
from helpers.constants import WebPageUrl
import allure
import re


class DevicesPage():

    def __init__(self, page: Page) -> None:
        self.page = page
        self.device_input = page.locator("#SearchDeviceId")
        self.online_status = page.locator("#SearchProblemFree")
        self.search_button = page.get_by_role("button", name="Filtern")
        self.device_item = page.get_by_text(re.compile(r'1097[0-9a-z]{8}'))
        self.device_ip_address = page.get_by_text(re.compile(r'[0-9]{3}.[0-9]{3}.[0-9]{1,3}.[0-9]{1,3}'))


    @allure.step('And select specific device')
    def select_device(self, device_id) -> None:
        self.device_input.fill(device_id)
        self.online_status.select_option("-1")
        self.search_button.click()
        self.device_item.click()
        self.page.wait_for_url(WebPageUrl.SPECIFIC_DEVICE_PAGE + device_id)
