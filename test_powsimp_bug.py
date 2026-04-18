import pytest
from sympy import *

def test_issue_reproduction():
    """Test that simplify preserves equivalence for complex power expressions."""
    x = Symbol('x')
    e = (-x/4 - S(1)/12)**x - 1
    f = simplify(e)
    
    # Test with x = 9/5 where the bug manifests
    a = S(9)/5
    
    # Evaluate both expressions numerically
    original_val = N(e.subs(x, a))
    simplified_val = N(f.subs(x, a))
    
    # The original should be real, simplified should not be (showing the bug)
    # Original: -1.32255049319339 (real)
    # Simplified: -0.739051169462523 - 0.189590423018741*I (complex)
    
    # Check that both expressions should give the same result
    # This will fail because they don't match due to the bug
    assert abs(original_val - simplified_val) < 1e-10, f"Original: {original_val}, Simplified: {simplified_val}"