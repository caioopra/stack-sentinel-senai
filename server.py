import os
import httpx
from pydantic import BaseModel

BASE = os.getenv("STACK_SENTINEL_API", "http://localhost:8000")

class TicketContext(BaseModel):
    summary: str
    severity: str
    service: str
    status: str

def fetch_ticket_context(ticket_id: str) -> TicketContext:
    """Retorna summary, severity, service e status de um ticket."""
    try:
        r = httpx.get(f"{BASE}/tickets/{ticket_id}", timeout=5)
        r.raise_for_status()
    except httpx.HTTPError:
        raise ValueError(f"ticket {ticket_id} indisponível")
    return TicketContext(**r.json())
