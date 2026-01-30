"""Módulo principal da Fast API.

Este módulo contém a configuração principal da aplicação FastAPI
e as rotas da API.
"""

from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

from fast_api.schemas import Message

app = FastAPI(
    title='Fast API',
    description='API desenvolvida com FastAPI',
    version='0.1.0',
)


# Rota raiz da API
@app.get(
    '/',
    status_code=HTTPStatus.OK,
    response_class=JSONResponse,
    response_model=Message,
)
def read_root() -> JSONResponse:
    """Retorna uma mensagem de boas-vindas."""
    # return Message(message='Hello, World!')
    return {'message': 'Hello, World!'}


# Rota HTML (Exercício 2)
@app.get(
    '/html',
    status_code=HTTPStatus.OK,
    response_class=HTMLResponse,
)
def read_html() -> HTMLResponse:
    """Retorna uma página HTML."""
    return HTMLResponse(
        content="""
        <html>
            <head>
                <title>Nosso olá mundo!</title>
            </head>
            <body>
                <h1> Olá Mundo </h1>
            </body>
        </html>"""
    )
