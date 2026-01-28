"""Módulo principal da API Aruma.

Este módulo contém a configuração principal da aplicação FastAPI
e as rotas da API.
"""

from fastapi import FastAPI

app = FastAPI(
    title='Aruma API',
    description='API do projeto Aruma',
    version='0.1.0',
)


@app.get('/')
def read_root() -> dict[str, str]:
    """Retorna uma mensagem de boas-vindas.

    Returns:
        dict[str, str]: Dicionário com a mensagem de boas-vindas.
    """
    return {'message': 'Hello, World!'}
