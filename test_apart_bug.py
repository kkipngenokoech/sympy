import pytest
from sympy import symbols, apart, Rational
from sympy.abc import x

def test_issue_reproduction():
    """Test that apart produces correct partial fraction decomposition."""
    # This is a case where apart might produce wrong coefficients
    # The correct partial fraction decomposition of 1/((x-1)*(x-2)) should be:
    # 1/(x-2) - 1/(x-1)
    expr = 1/((x-1)*(x-2))
    result = apart(expr, x)
    
    # Verify by expanding back - if apart is correct, this should equal the original
    from sympy import expand, simplify
    expanded = simplify(result.as_numer_denom()[0]/result.as_numer_denom()[1])
    original = simplify(expr.as_numer_denom()[0]/expr.as_numer_denom()[1])
    
    # The bug would manifest as incorrect coefficients in the partial fraction
    # Let's check a specific case that's known to potentially fail
    expected = -1/(x-1) + 1/(x-2)
    assert simplify(result - expected) == 0, f"Expected {expected}, got {result}"