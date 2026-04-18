import sympy as sp
from sympy import cos, sin, sqrt, trigsimp, symbols, I

def test_issue_reproduction():
    # Test with a general complex symbol (no assumptions)
    x = symbols('x')
    expr = cos(x) + sqrt(sin(x)**2)
    
    # The buggy behavior: trigsimp incorrectly simplifies this
    simplified = trigsimp(expr)
    
    # For complex x, sqrt(sin(x)**2) should NOT simplify to sin(x)
    # because sqrt(z**2) = |z| for complex z, not z
    # So the expression should remain as cos(x) + sqrt(sin(x)**2)
    # or be simplified to cos(x) + Abs(sin(x))
    
    # Test that demonstrates the bug: if trigsimp incorrectly
    # simplifies to cos(x) + sin(x), then substituting x = 3*pi/2
    # should give different results
    test_val = 3*sp.pi/2
    
    original_result = expr.subs(x, test_val)
    simplified_result = simplified.subs(x, test_val)
    
    # At x = 3*pi/2: cos(3*pi/2) = 0, sin(3*pi/2) = -1
    # So cos(x) + sqrt(sin(x)**2) = 0 + sqrt((-1)**2) = 0 + 1 = 1
    # But cos(x) + sin(x) = 0 + (-1) = -1
    
    expected = 1  # cos(3*pi/2) + |sin(3*pi/2)| = 0 + 1
    
    # The test fails if trigsimp incorrectly simplified the expression
    assert simplified_result == expected, f"trigsimp incorrectly simplified sqrt(sin(x)**2) for complex x. Got {simplified_result}, expected {expected}"