import pytest

from ..app.api import create_app


class TrackingService:
    def __init__(self):
        self.called = False
        self.calls = []

    def perform(self, operation, a, b):
        self.called = True
        self.calls.append((operation, a, b))
        return 0.0


@pytest.fixture
def tracking_service():
    return TrackingService()


@pytest.fixture
def api_client(tracking_service):
    app = create_app(service=tracking_service)
    return app.test_client(), tracking_service


@pytest.mark.parametrize("payload", [
    {"operation": "add", "a": "x", "b": 2},
    {"operation": 123, "a": 1, "b": 2},
    {"operation": "add", "a": 1},
    "not-a-json",
])
def test_calculate_invalid_input_returns_400(api_client, payload):
    client, service = api_client
    response = client.post("/api/calculate", json=payload)

    assert response.status_code == 400
    assert not service.called
