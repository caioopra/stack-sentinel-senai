from typing import TypedDict


class AgentState(TypedDict):
    user_input: str
    intent: str | None
    ticket_id: str | None
    build_id: str | None
    context: dict | None
    error: str | None
    final_answer: str | None
