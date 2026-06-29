# stack-sentinel

Hub de investigação técnica para devs. Serviço mockado (FastAPI), tools tipadas,
um MCP Server e os primeiros nós de um agente em LangGraph.

O código vive no pacote `src/stack_sentinel/`.

## Rodar

```bash
uv run uvicorn stack_sentinel.mock.api:app --port 8000   # sobe a mock API (necessária p/ as tools/resource)
uv run mcp dev src/stack_sentinel/mcp_server/server.py   # abre o MCP Inspector pra chamar a tool
uv run pytest                                            # roda os testes
```

Os testes sobem a mock API sozinhos (uvicorn em background), então
`uv run pytest` passa verde sem precisar subir nada manualmente.

A base da API usada pelas tools vem de `STACK_SENTINEL_API`
(default `http://localhost:8000`).

## Demos da Aula 2

```bash
uv run mcp dev src/stack_sentinel/mcp_server/server.py   # Demo 1: Inspector (Resources/Prompts)
uv run python -m stack_sentinel.agent.graph_min          # Demo 2: grafo mínimo
uv run pytest tests/test_classify.py -v                  # Demo 3: classify com FakeLLM
uv run pytest                                            # tudo verde
```

- **Demo 1** — `stack_sentinel/mcp_server/server.py` expõe a tool `fetch_build_status`, o resource
  `docs://severity-policy` e o prompt `incident_triage` (precisa da mock API no ar).
- **Demo 2** — `stack_sentinel/agent/graph_min.py`: grafo mínimo do LangGraph (`START → echo → END`)
  que imprime o state final.
- **Demo 3** — `classify_intent_node` (em `stack_sentinel/agent/classify.py`) usa structured output
  (`IntentResult`) pra classificar a intenção. Os testes injetam o `FakeClassifier`
  (`stack_sentinel/agent/fakes.py`), que espelha a interface do chat model real, sem exigir chave de API.

### LLM real (opcional)

Em produção, no lugar do `FakeClassifier`, injeta-se um chat model de verdade —
o `classify_intent_node` não muda, só muda quem é o `llm`:

```python
from langchain.chat_models import init_chat_model
llm = init_chat_model("google_genai:gemini-2.5-flash")  # Gemini free tier
# ou
from langchain_ollama import ChatOllama
llm = ChatOllama(model="llama3.1")                       # Ollama local
```
