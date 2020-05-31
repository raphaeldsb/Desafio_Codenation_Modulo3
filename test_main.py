from main import get_temperature
import pytest
import requests


class MockResponse:
    def __init__(self, temperature):
        self.__temperature = temperature

    def json(self):
        return {"currently": {"temperature": self.__temperature}}


parametrize = [
    (-14.235004, -51.92528, 16, 62),
    (-22.970722, -43.182365, 0, 32),
    (39.3998718, -8.2244539, 30, 86)
]


@pytest.mark.parametrize(
    "lat, lng, expected, temperature", parametrize)
def test_get_temperature_by_lat_lng(
        lat, lng, expected, temperature, monkeypatch):

    def mock_get(* args, ** kwargs):
        return MockResponse(temperature)

    monkeypatch.setattr(requests, "get", mock_get)

    result = get_temperature(lat, lng)

    assert result == expected
