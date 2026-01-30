# Aruma API

API REST desenvolvida com FastAPI para o projeto Aruma.

## Descrição

Este projeto é uma API moderna e de alta performance construída com FastAPI, seguindo as melhores práticas de desenvolvimento Python (PEP-8, PEP-257, PEP-484).

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
cd aruma_api
```

### 4. Configurar o ambiente

```bash
poetry env use 3.13
poetry install
```

## Rotas da API

| Método | Rota   | Descrição                    | Resposta        |
|--------|--------|------------------------------|-----------------|
| GET    | `/`    | Mensagem de boas-vindas      | JSON            |
| GET    | `/html`| Página HTML "Olá Mundo"      | HTML            |

- **GET /** — Retorna `{"message": "Hello, World!"}` (Content-Type: application/json).
- **GET /html** — Retorna uma página HTML com título "Nosso olá mundo!" e `<h1>Olá Mundo</h1>`.

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
fastapi dev aruma_api/app.py
```

A API estará disponível em: http://127.0.0.1:8000

### Documentação interativa

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## Comandos Disponíveis (Taskipy)

| Comando | Descrição |
|---------|-----------|
| `task run` | Inicia o servidor de desenvolvimento |
| `task lint` | Verifica o código com ruff |
| `task format` | Formata o código com ruff |
| `task test` | Executa os testes com cobertura |

## Estrutura do Projeto

```
aruma_api/
├── aruma_api/
│   ├── __init__.py
│   ├── app.py          # Aplicação principal e rotas
│   └── schemas.py      # Modelos Pydantic (ex.: Message)
├── tests/
│   ├── __init__.py
│   └── test_app.py     # Testes da aplicação
├── pyproject.toml      # Configurações do projeto
├── poetry.lock         # Lock das dependências
└── README.md
```

## Ferramentas de Desenvolvimento

- **ruff**: Linter e formatador de código (PEP-8)
- **pytest**: Framework de testes
- **pytest-cov**: Cobertura de testes
- **taskipy**: Automação de tarefas

## Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova feature'`)
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