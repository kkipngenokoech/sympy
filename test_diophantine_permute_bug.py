import pytest
from sympy import symbols, diophantine

def test_issue_reproduction():
    """Test that diophantine with permute=True gives complete results regardless of symbol order."""
    m, n = symbols('m n')
    equation = n**4 + m**4 - 2**4 - 3**4
    
    # Get results with different symbol orders
    result_mn = diophantine(equation, syms=(m, n), permute=True)
    result_nm = diophantine(equation, syms=(n, m), permute=True)
    
    # Convert tuples to sets of frozensets to compare regardless of order
    # Each solution tuple (a, b) with syms=(m, n) corresponds to m=a, n=b
    # Each solution tuple (c, d) with syms=(n, m) corresponds to n=c, m=d
    
    solutions_mn = set()
    for sol in result_mn:
        # sol is (m_val, n_val)
        solutions_mn.add(frozenset([('m', sol[0]), ('n', sol[1])]))
    
    solutions_nm = set()
    for sol in result_nm:
        # sol is (n_val, m_val) 
        solutions_nm.add(frozenset([('n', sol[0]), ('m', sol[1])]))
    
    # Both should give the same set of solutions
    assert solutions_mn == solutions_nm, f"Symbol order affects results: {result_mn} vs {result_nm}"