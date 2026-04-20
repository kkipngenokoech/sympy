import pytest
from sympy import Symbol, cos, I, simplify

def test_issue_reproduction():
    """Test that simplify(cos(x)**I) raises TypeError due to invalid complex comparison."""
    x = Symbol('x')
    expr = cos(x)**I
    
    # This should raise TypeError: Invalid comparison of complex I
    with pytest.raises(TypeError, match="Invalid comparison of complex"):
        simplify(expr)