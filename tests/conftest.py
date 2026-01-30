"""Fixtures para os testes."""

import pytest
from fastapi.testclient import TestClient

from fast_api.app import app


@pytest.fixture
def client() -> TestClient:
    """Fixture para criar um cliente HTTP para testar a API."""
    # Arrange
    return TestClient(app)
