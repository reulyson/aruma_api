# Fast API

API REST desenvolvida com FastAPI.

## Descrição

Este projeto é uma API moderna e de alta performance construída com **FastAPI**, seguindo as melhores práticas de desenvolvimento Python (PEP-8, PEP-257, PEP-484). Oferece um CRUD de usuários em memória e documentação OpenAPI automática.

## Pré-requisitos

- **Python**: 3.13+
- **pipx**: Para instalar ferramentas Python isoladas
- **Poetry**: Para gerenciamento de dependências

## Instalação

### 1. Instalar o pipx

```bash
pip install --user pipx
pipx ensurepath
```

### 2. Instalar o Poetry

```bash
pipx install poetry
pipx inject poetry poetry-plugin-shell
```

### 3. Clonar e configurar o projeto

```bash
git clone <url-do-repositorio>
cd fast_api
```

### 4. Configurar o ambiente

```bash
poetry env use 3.13
poetry install
```

## Rotas da API

| Método   | Rota           | Descrição                    | Resposta   |
|----------|----------------|------------------------------|------------|
| GET      | `/`            | Mensagem de boas-vindas      | JSON       |
| POST     | `/users/`      | Cria um usuário               | 201 + JSON |
| GET      | `/users/`      | Lista todos os usuários       | JSON       |
| GET      | `/users/{id}`  | Retorna um usuário pelo id    | JSON / 404 |
| PUT      | `/users/{id}`  | Atualiza um usuário pelo id   | JSON / 404 |
| DELETE   | `/users/{id}`  | Remove um usuário pelo id     | JSON / 404 |

- **GET /** — Retorna `{"message": "Hello, World!"}`.
- **POST /users/** — Body: `username`, `email`, `password`. Retorna o usuário criado (sem senha).
- **GET /users/** — Retorna `{"users": [...]}`.
- **GET /users/{user_id}** — Retorna o usuário ou 404.
- **PUT /users/{user_id}** — Body: `username`, `email`, `password`. Retorna o usuário atualizado ou 404.
- **DELETE /users/{user_id}** — Retorna o usuário removido ou 404.

## Como Usar

### Ativar o ambiente virtual

```bash
poetry shell
```

### Iniciar o servidor de desenvolvimento

```bash
task run
```

Ou diretamente:

```bash
fastapi dev fast_api/app.py
```

A API estará disponível em: **http://127.0.0.1:8000**

### Documentação interativa

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## Comandos Disponíveis (Taskipy)

| Comando       | Descrição                          |
|---------------|------------------------------------|
| `task run`    | Inicia o servidor de desenvolvimento |
| `task lint`   | Verifica o código com Ruff         |
| `task format` | Formata o código com Ruff          |
| `task test`   | Executa os testes com cobertura    |

## Estrutura do Projeto

```
fast_api/
├── fast_api/
│   ├── __init__.py
│   ├── app.py          # Aplicação principal e rotas
│   └── schemas.py      # Modelos Pydantic (Message, UserSchema, UserPublic, UserList, ErrorDetail)
├── tests/
│   ├── conftest.py     # Fixtures (cliente de teste)
│   └── test_app.py     # Testes da aplicação
├── pyproject.toml     # Configurações do projeto
├── poetry.lock        # Lock das dependências
└── README.md
```

## Ferramentas de Desenvolvimento

- **Ruff**: Linter e formatador de código (PEP-8, linha ≤ 79 caracteres, aspas simples)
- **pytest**: Framework de testes
- **pytest-cov**: Cobertura de testes
- **taskipy**: Automação de tarefas (lint, format, test, run)

## Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Faça commit das suas alterações (`git commit -m 'feat: adiciona nova feature'`)
4. Faça push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

### Padrões de Código

- Siga a **PEP-8** para estilo de código
- Use **aspas simples** para strings
- Mantenha linhas com no máximo **79 caracteres**
- Adicione **docstrings** (PEP-257) em módulos, classes e funções
- Use **type hints** (PEP-484) em todas as funções

## Licença

Este projeto está sob a licença MIT.
