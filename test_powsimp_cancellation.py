import sympy
from sympy import Symbol, powsimp

def test_issue_reproduction():
    x = Symbol('x')
    expr = -0.5*x**2.5 + 0.5*x**2.5
    result = powsimp(expr)
    # This should simplify to 0, but currently doesn't
    assert result == 0, f"Expected 0, but got {result}"