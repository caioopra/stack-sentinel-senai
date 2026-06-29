# stack-sentinel

Hub de investigação técnica para devs. Parte 1: serviço mockado (FastAPI),
uma tool tipada (`fetch_ticket_context`) e um MCP Server mínimo expondo essa tool.

## Rodar

```bash
uv run uvicorn mock_api:app --port 8000   # sobe a mock API
uv run mcp dev server.py                  # abre o MCP Inspector pra chamar a tool
uv run pytest                             # roda os testes
```

Os testes sobem a mock API sozinhos (uvicorn em background), então
`uv run pytest` passa verde sem precisar subir nada manualmente.

A base da API usada pela tool vem de `STACK_SENTINEL_API`
(default `http://localhost:8000`).
