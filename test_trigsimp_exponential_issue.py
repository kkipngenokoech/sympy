import pytest
from sympy import symbols, exp, I, trigsimp, sin, sinc, simplify

def test_issue_reproduction():
    k = symbols('k')
    
    # Test case 1: (exp(I*k) - exp(-I*k))/(2*I) should simplify to sin(k)
    expr1 = (exp(I*k) - exp(-I*k))/(2*I)
    result1 = trigsimp(expr1)
    expected1 = sin(k)
    
    # This should pass once the issue is fixed
    assert result1 == expected1, f"Expected {expected1}, got {result1}"
    
    # Test case 2: (exp(I*k) - exp(-I*k))/(2*I*k) should simplify to sinc(k)
    expr2 = (exp(I*k) - exp(-I*k))/(2*I*k)
    result2 = trigsimp(expr2)
    expected2 = sinc(k)
    
    # This should pass once the issue is fixed
    assert result2 == expected2, f"Expected {expected2}, got {result2}"