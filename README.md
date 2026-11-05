# api-contract-tests

![API Tests](https://github.com/MateusCerqueiraG/api-contract-tests/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11%20%7C%203.12-3776AB?logo=python&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?logo=pytest&logoColor=white)

Testes automatizados de **API REST** com **Python + pytest + requests**, validando o **contrato** das respostas via **JSON Schema** (`jsonschema`), o ciclo **CRUD** completo, autenticação e cenários negativos. Roda em **CI (GitHub Actions)** numa matriz de versões do Python, com relatório **Allure**.

> **Alvo sob teste:** [restful-booker](https://restful-booker.herokuapp.com) — API pública de prática de QA (reservas de hotel). Nenhum sistema real ou privado é tocado.

## O que a suíte cobre
- **Health check** — `GET /ping` (201)
- **Autenticação** — `POST /auth` (token válido e credenciais inválidas)
- **CRUD completo** — criar → ler → atualizar (PUT) → atualizar parcial (PATCH) → deletar → confirmar 404
- **Contrato (JSON Schema)** — valida a *forma* das respostas (booking, criação, listagem)
- **Negativos** — 404 (inexistente), 500 (payload incompleto), 403 (escrita sem auth)

## Técnicas e boas práticas demonstradas
- **Contract testing** com `jsonschema` — asserta o schema, não só o status code
- **Fixtures** com setup/teardown e **limpeza automática** de dados (nenhum resíduo no ambiente)
- **Autenticação por token** reutilizada por sessão
- **Matriz de versões** (Python 3.11 e 3.12) no CI
- **Rerun** de falhas de rede (API externa pode ter cold-start) + **timeout** por request

## Estrutura
```
api-contract-tests/
├── conftest.py              # fixtures: base_url, session, token, created_booking (com teardown)
├── schemas/
│   └── booking.py           # JSON Schemas do contrato da API
├── tests/
│   ├── test_health.py
│   ├── test_auth.py
│   ├── test_booking_crud.py # ciclo de vida completo
│   ├── test_contract.py     # validação de schema
│   └── test_negative.py     # 404 / 500 / 403
├── .github/workflows/tests.yml
├── pytest.ini
└── requirements.txt
```

## Como rodar localmente
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest                       # roda tudo
pytest -k contract           # só os testes de contrato
```

## Relatório Allure
```bash
pytest --alluredir=allure-results
allure serve allure-results
```
**Publicado:** a cada push na `main`, o CI gera e publica o relatório em `gh-pages`:
👉 **https://mateuscerqueirag.github.io/api-contract-tests/**
> Habilitar em *Settings → Pages → Deploy from a branch → `gh-pages` / root*.

---
*Projeto de portfólio — foco em testes de contrato de API. Alvo exclusivamente o app público de demonstração restful-booker.*
