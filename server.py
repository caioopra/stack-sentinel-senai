import os
import httpx
from pydantic import BaseModel
from mcp.server.fastmcp import FastMCP

BASE = os.getenv("STACK_SENTINEL_API", "http://localhost:8000")
mcp = FastMCP("stack-sentinel")


class TicketContext(BaseModel):
    summary: str
    severity: str
    service: str
    status: str


@mcp.tool()
def fetch_ticket_context(ticket_id: str) -> TicketContext:
    """Retorna summary, severity, service e status de um ticket."""
    try:
        r = httpx.get(f"{BASE}/tickets/{ticket_id}", timeout=5)
        r.raise_for_status()
    except httpx.HTTPError:
        raise ValueError(f"ticket {ticket_id} indisponível")
    return TicketContext(**r.json())


class BuildStatus(BaseModel):
    service: str
    status: str
    branch: str
    commit: str


@mcp.tool()
def fetch_build_status(build_id: str) -> BuildStatus:
    """Retorna service, status, branch e commit de um build."""
    try:
        r = httpx.get(f"{BASE}/builds/{build_id}", timeout=5)
        r.raise_for_status()
    except httpx.HTTPError:
        raise ValueError(f"build {build_id} indisponível")
    return BuildStatus(**r.json())


@mcp.resource("docs://severity-policy")
def severity_policy() -> str:
    """Política de severidade de incidentes (contexto só-leitura)."""
    r = httpx.get(f"{BASE}/docs/severity-policy", timeout=5)
    r.raise_for_status()
    return r.json()["content"]


if __name__ == "__main__":
    mcp.run()
