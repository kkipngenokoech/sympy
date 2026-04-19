import sympy as sy

def test_issue_reproduction():
    # Test the specific case mentioned in the issue
    M1 = sy.Matrix.zeros(0, 0)
    M2 = sy.Matrix.zeros(0, 3)
    M3 = sy.Matrix.zeros(0, 3)
    
    # This should return (0, 6) according to sympy 1.0 behavior
    # but currently returns (0, 3) in sympy 1.1
    result = sy.Matrix.hstack(M1, M2, M3)
    
    # The expected behavior from sympy 1.0
    assert result.shape == (0, 6), f"Expected (0, 6) but got {result.shape}"
    
    # Also test the case that works correctly
    M4 = sy.Matrix.zeros(1, 0)
    M5 = sy.Matrix.zeros(1, 3)
    M6 = sy.Matrix.zeros(1, 3)
    
    result2 = sy.Matrix.hstack(M4, M5, M6)
    assert result2.shape == (1, 6), f"Expected (1, 6) but got {result2.shape}"