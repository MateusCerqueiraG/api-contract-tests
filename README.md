<div align="center">

# 🔌 api-contract-tests

**Testes de Contrato de API REST** &nbsp;·&nbsp; Python &nbsp;·&nbsp; pytest &nbsp;·&nbsp; requests &nbsp;·&nbsp; JSON Schema

[![API Tests](https://github.com/MateusCerqueiraG/api-contract-tests/actions/workflows/tests.yml/badge.svg)](https://github.com/MateusCerqueiraG/api-contract-tests/actions/workflows/tests.yml)
&nbsp;
[![Relatório Allure](https://img.shields.io/badge/📊_Relatório-Allure_ao_vivo-5fd0e6?style=flat&labelColor=103a4e)](https://mateuscerqueirag.github.io/api-contract-tests/)

![Python](https://img.shields.io/badge/Python-3.11_|_3.12-3776AB?logo=python&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?logo=pytest&logoColor=white)
![requests](https://img.shields.io/badge/requests-2C2D72?logo=python&logoColor=white)
![JSON Schema](https://img.shields.io/badge/JSON_Schema-contract-6BA539)

</div>

---

Suíte que valida uma **API REST** de ponta a ponta — não só o status code, mas o **contrato** (a forma) das respostas via **JSON Schema** — cobrindo o ciclo **CRUD** completo, autenticação e cenários negativos, rodando em **CI** numa matriz de versões do Python.

> 🎯 **Alvo sob teste:** [restful-booker](https://restful-booker.herokuapp.com) — API **pública, feita para prática de QA**. Nenhum sistema real ou privado é tocado.

## ✅ O que a suíte cobre

| Área | Verificações |
|:--|:--|
| 🩺 **Health** | `GET /ping` responde 201 |
| 🔑 **Autenticação** | token válido · credenciais inválidas |
| 🔁 **CRUD** | criar → ler → PUT → PATCH → deletar → confirmar 404 |
| 📐 **Contrato** | JSON Schema da reserva, da criação e da listagem |
| 🚫 **Negativos** | 404 (inexistente) · 500 (payload incompleto) · 403 (escrita sem auth) |

<div align="center">

**12 testes &nbsp;·&nbsp; Python 3.11 + 3.12 &nbsp;·&nbsp; 100% verde**

</div>

## 🧰 Stack & práticas

- 📐 **Contract testing** com `jsonschema` — asserta o *schema* da resposta, não só o status
- 🧪 **Fixtures** com setup/teardown e **limpeza automática** (nenhum resíduo no ambiente)
- 🔑 **Auth por token** reutilizada por sessão
- 🧮 **Matriz de versões** — Python 3.11 e 3.12 no CI
- 🔁 **Anti-flaky** — rerun de falhas de rede + timeout por request

## 📁 Estrutura

```
conftest.py              # fixtures: base_url, session, token, created_booking (com teardown)
schemas/booking.py       # JSON Schemas do contrato da API
tests/
├── test_health.py
├── test_auth.py
├── test_booking_crud.py # ciclo de vida completo
├── test_contract.py     # validação de schema
└── test_negative.py     # 404 / 500 / 403
.github/workflows/tests.yml
```

## ▶️ Como rodar

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

pytest                   # roda tudo
pytest -k contract       # só os testes de contrato
```

## 📊 Relatório Allure

Publicado automaticamente a cada push na `main`:

### 👉 **[mateuscerqueirag.github.io/api-contract-tests](https://mateuscerqueirag.github.io/api-contract-tests/)**

Localmente:
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

---

<div align="center">
<sub>Projeto de portfólio · foco em testes de contrato de API · alvo exclusivamente o app público restful-booker</sub>
</div>
