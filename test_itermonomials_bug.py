import sympy as sp
from sympy.polys.monomials import itermonomials
from sympy.polys.orderings import monomial_key

def test_issue_reproduction():
    x1, x2, x3 = sp.symbols('x1 x2 x3')
    variables = [x1, x2, x3]
    
    # Generate monomials with total degree exactly 3 (min_degrees=3, max_degrees=3)
    monomials = list(itermonomials(variables, 3, 3))
    
    # Sort for consistent comparison
    monomials_sorted = sorted(monomials, key=lambda x: str(x))
    
    # Expected monomials with total degree 3:
    # x1**3, x2**3, x3**3, x1**2*x2, x1**2*x3, x2**2*x1, x2**2*x3, x3**2*x1, x3**2*x2, x1*x2*x3
    expected = [
        x1**3, x2**3, x3**3,
        x1**2*x2, x1**2*x3, x2**2*x1, x2**2*x3, x3**2*x1, x3**2*x2,
        x1*x2*x3
    ]
    expected_sorted = sorted(expected, key=lambda x: str(x))
    
    # The bug: current implementation only returns [x1**3, x2**3, x3**3]
    # Missing monomials like x1*x2**2, x1**2*x2, x1*x2*x3, etc.
    assert len(monomials) == len(expected), f"Expected {len(expected)} monomials, got {len(monomials)}"
    assert set(monomials) == set(expected), f"Missing monomials: {set(expected) - set(monomials)}"