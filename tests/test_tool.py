import pytest
from server import fetch_ticket_context

def test_ticket_existente():
    ctx = fetch_ticket_context("TCK-101")
    assert ctx.severity in {"low", "medium", "high", "critical"}

def test_ticket_inexistente():
    with pytest.raises(ValueError):
        fetch_ticket_context("NAO-EXISTE")
