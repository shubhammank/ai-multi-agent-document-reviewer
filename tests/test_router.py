import pytest
from routing.router import Router

@pytest.fixture
def router():
    return Router()

def test_table_routes_to_evidence(router):
    chunk = {"text": "Scope 1 | 200 | 180", "type": "table_row", "density": 0.5}
    assert router.route(chunk) == "evidence"

def test_keyword_routing(router):
    chunk = {"text": "The baseline value is not provided.", "type": "paragraph", "density": 0.1}
    assert router.route(chunk) == "evidence"

def test_density_routing(router):
    chunk = {"text": "This is unclear.", "type": "paragraph", "density": 0.02}
    assert router.route(chunk) == "proofreading" or router.route(chunk) == "clarification"
