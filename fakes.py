from classify import IntentResult


class FakeClassifier:
    """LLM falso e deterministico: respeita with_structured_output/invoke."""

    def with_structured_output(self, schema):
        return self

    def invoke(self, messages):
        texto = messages[-1][1].lower()
        if "ticket" in texto or "tck" in texto:
            return IntentResult(intent="ticket")
        if "build" in texto or "bld" in texto:
            return IntentResult(intent="build")
        if "incidente" in texto or "doc" in texto or "severidade" in texto:
            return IntentResult(intent="docs")
        return IntentResult(intent="unknown")
