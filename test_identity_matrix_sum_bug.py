import sympy as sp
from sympy import symbols, MatrixSymbol, Q, assuming, Identity

def test_issue_reproduction():
    # Test case 1: Direct identity matrix sum
    n = symbols('n', positive=True, integer=True)
    I = Identity(n)
    
    # Sum of all elements in an n×n identity matrix should be n
    total_sum = sum(I)
    
    # This should equal n, but currently returns 0 (the bug)
    assert total_sum == n, f"Expected {n}, but got {total_sum}"
    
    # Test case 2: Identity matrix from orthogonal assumption (as mentioned in issue)
    M = MatrixSymbol('M', n, n)
    with assuming(Q.orthogonal(M)):
        identity_expr = M.T * M
        # This should also sum to n
        identity_sum = sum(identity_expr)
        assert identity_sum == n, f"Expected {n} for orthogonal case, but got {identity_sum}"