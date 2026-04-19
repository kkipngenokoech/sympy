from sympy import symbols, apart, S
from sympy.abc import x, y, t

def test_issue_reproduction():
    # Test case that likely exposes the bug with symbolic coefficients
    # This should test partial fraction decomposition with symbolic parameters
    expr = y / ((x + 1) * (x + y))
    result = apart(expr, x)
    
    # The correct partial fraction decomposition should be:
    # y/((y-1)*(x+1)) - y/((y-1)*(x+y)) when y != 1
    # But the current implementation likely produces an incorrect result
    expected = y/((y-1)*(x+1)) - y/((y-1)*(x+y))
    
    # Verify by expanding both expressions - they should be equal
    from sympy import simplify, expand
    original_expanded = expand(expr)
    result_expanded = expand(result)
    expected_expanded = expand(expected)
    
    # The bug is that result != expected when it should be
    assert simplify(result_expanded - original_expanded) == 0, "Result should equal original"
    assert simplify(expected_expanded - original_expanded) == 0, "Expected should equal original"
    
    # This assertion should fail on buggy code if apart gives wrong result
    assert simplify(result - expected) == 0, f"apart() gave {result}, expected {expected}"