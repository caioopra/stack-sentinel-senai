from stack_sentinel.agent.state import AgentState
from stack_sentinel.agent.classify import classify_intent_node
from stack_sentinel.agent.fakes import FakeClassifier

llm = FakeClassifier()


def run(q: str) -> str:
    state: AgentState = {
        "user_input": q, "intent": None, "ticket_id": None, "build_id": None,
        "context": None, "error": None, "final_answer": None,
    }
    return classify_intent_node(state, llm)["intent"]


def test_ticket():
    assert run("Qual o status do ticket TCK-101?") == "ticket"


def test_build():
    assert run("O build BLD-203 esta quebrado?") == "build"


def test_docs():
    assert run("Como trato um incidente critico?") == "docs"


def test_unknown():
    assert run("Qual a capital da Franca?") == "unknown"
