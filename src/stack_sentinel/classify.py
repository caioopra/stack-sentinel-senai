from typing import Literal
from pydantic import BaseModel, Field
from stack_sentinel.agent_state import AgentState


class IntentResult(BaseModel):
    intent: Literal["ticket", "build", "docs", "unknown"] = Field(
        description="Categoria da pergunta do usuario."
    )


SYSTEM = (
    "Classifique a pergunta do usuario em UMA destas categorias: "
    "ticket, build, docs, unknown. "
    "Use 'unknown' se a pergunta estiver fora do dominio de suporte tecnico."
)


def classify_intent_node(state: AgentState, llm) -> dict:
    structured = llm.with_structured_output(IntentResult)
    result = structured.invoke([
        ("system", SYSTEM),
        ("user", state["user_input"]),
    ])
    return {"intent": result.intent}
