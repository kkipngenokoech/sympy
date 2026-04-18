import sympy
from sympy import Array, Matrix

def test_issue_reproduction():
    # This should work (Matrix handles empty case)
    empty_matrix = Matrix([])
    assert empty_matrix.shape == (0, 0)
    
    # This currently fails with "ValueError: not enough values to unpack (expected 2, got 0)"
    empty_array = Array([])
    assert empty_array.shape == (0,)