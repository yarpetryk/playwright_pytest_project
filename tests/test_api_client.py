import pytest
from playwright.sync_api import APIRequestContext


class TestApiClient:
    @pytest.mark.api
    def test_api_devices(self,
                         api_request_context: APIRequestContext) -> None:
        res = api_request_context.get("/api/3.0/devices")
        data = res.json()
        assert len(data) > 0
        for el in data:
            assert el['division'] in range(5)

    @pytest.mark.api
    def test_api_operating(self,
                           api_request_context: APIRequestContext) -> None:
        body = {
            "deviceId": "1097bd6e54f4",
            "extended": True
        }
        res = api_request_context.post("/api/3.0//current/0/operating", data=body)
        data = res.json()
        assert data['watt'] < 100

