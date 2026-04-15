import sympy as sp
from sympy import symbols, exp, I, sin, simplify, pi

def test_issue_reproduction():
    k = symbols('k')
    
    # Test case 1: (exp(I*k) - exp(-I*k))/(2*I) should simplify to sin(k)
    expr1 = (exp(I*k) - exp(-I*k))/(2*I)
    simplified1 = simplify(expr1)
    
    # This should equal sin(k) but currently doesn't get simplified
    expected1 = sin(k)
    assert simplified1 == expected1, f"Expected {expected1}, got {simplified1}"
    
    # Test case 2: sin(k)/k should be recognizable as sinc(k)
    # Note: SymPy doesn't have a built-in sinc function, but the issue mentions
    # it would be "awesome" if this could be recognized
    expr2 = sin(k)/k
    # This is more about the exponential form leading to sinc, but let's test
    # the basic exponential to sin conversion first
    
    # The main issue is that exponential forms aren't being converted to trig forms
    # during simplification, so the test focuses on that