from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    user_input: str
    reply: str


def echo(state: State) -> dict:
    return {"reply": f"recebi: {state['user_input']}"}


def build():
    g = StateGraph(State)
    g.add_node("echo", echo)
    g.add_edge(START, "echo")
    g.add_edge("echo", END)
    return g.compile()


if __name__ == "__main__":
    app = build()
    out = app.invoke({"user_input": "oi", "reply": ""})
    print(out)
