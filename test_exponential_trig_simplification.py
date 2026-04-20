import pytest
from sympy import exp, I, sin, trigsimp, simplify
from sympy.abc import k

def test_issue_reproduction():
    # Test case 1: (exp(I*k) - exp(-I*k))/(2*I) should simplify to sin(k)
    expr1 = (exp(I*k) - exp(-I*k))/(2*I)
    result1 = trigsimp(expr1)
    expected1 = sin(k)
    
    # This should pass once the issue is fixed, but currently fails
    assert result1 == expected1, f"Expected {expected1}, got {result1}"
    
    # Also test with simplify to make sure it's not handled elsewhere
    result1_simplify = simplify(expr1)
    assert result1_simplify == expected1, f"Expected {expected1} from simplify, got {result1_simplify}"