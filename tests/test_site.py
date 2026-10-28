import pytest
from fastapi.testclient import TestClient

from app.main import app, EVENTS
from tests.test_events import make_event

client = TestClient(app)


@pytest.mark.parametrize("site, expected", [
    ("松年長照中心", 201),
    ("松年長照中心二館", 201),
    ("", 422),
    ("   ", 422),
], ids=["main", "branch2", "empty", "spaces"])
def test_site(site, expected):
    EVENTS.clear()
    r = client.post("/events", json=make_event(site=site))
    assert r.status_code == expected