import pytest
from logging import info, debug, warning, error


class TestBase:
    @pytest.mark.smoke_
    def test_positive_assert(self) -> None:
        assert 10 == 10
        info("Positive assertion")

    @pytest.mark.smoke
    def test_negative_assert(self) -> None:
        a = 9
        b = 10
        debug(f"a = {a}, but b = {b}")
        warning("WARNING: Negative assertion")
        error("ERROR: Negative assertion")
        assert a == b