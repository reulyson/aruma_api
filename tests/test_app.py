"""Testes para o módulo principal da API Aruma."""

from http import HTTPStatus

from fastapi.testclient import TestClient

from aruma_api.app import app


def test_read_root_deve_retornar_ok() -> None:
    """Testa se a rota raiz retorna status 200 OK."""
    client = TestClient(app)

    response = client.get('/')

    # HTTPStatus é um enum que contém os códigos de status HTTP
    assert response.status_code == HTTPStatus.OK


def test_read_root_deve_retornar_mensagem_hello_world() -> None:
    """Testa se a rota raiz retorna a mensagem Hello, World

    Esse teste tem 3 partes (AAA - Arrange, Act, Assert):
    1. Arrange: configurar o teste
    2. Act: executar o teste (o SUT - System Under Test)
    3. Assert: verificar se o resultado é o esperado
    """

    # Arrange
    # TestClient é o cliente HTTP para testar a API
    client = TestClient(app)

    # Act
    response = client.get('/')

    # Assert
    assert response.json() == {'message': 'Hello, World!'}
