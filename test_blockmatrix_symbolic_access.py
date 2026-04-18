import pytest
from sympy import symbols, MatrixSymbol, BlockMatrix

def test_issue_reproduction():
    """Test that BlockMatrix element access doesn't incorrectly simplify when indices are symbolic."""
    n, i = symbols('n, i', integer=True)
    A = MatrixSymbol('A', n, n)
    B = MatrixSymbol('B', n, n)
    C = BlockMatrix([[A], [B]])
    
    # Access element C[i, 0] - this should NOT simplify to A[i, 0]
    # because i could refer to elements in either block A or B
    result = C[i, 0]
    
    # The bug is that this incorrectly returns A[i, 0]
    # It should return something that doesn't assume which block i refers to
    assert str(result) != "A[i, 0]", f"Expected C[i, 0] to not simplify to A[i, 0], but got: {result}"