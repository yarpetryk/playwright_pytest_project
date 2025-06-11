import pytest

from playwright.sync_api import expect
from pages.start_page import StartPage


class TestUseEmail:
    @pytest.mark.smoke
    def test_user_email(self,
                        page,
                        login_set_up,
                        start_page: StartPage) -> None:
        expect(start_page.user_email).to_be_visible()