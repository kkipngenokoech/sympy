import sympy

def test_issue_reproduction():
    # Test that sympify with evaluate=False followed by simplify preserves the original form
    x = sympy.Symbol('x')
    
    # Parse with evaluate=False to preserve the original structure
    expr = sympy.sympify('4*ceiling(x/4 - 3/4)', evaluate=False)
    
    # Simplify should not change the structure when evaluate=False was used
    simplified = expr.simplify()
    
    # The expression should remain as 4*ceiling(x/4 - 3/4)
    # and NOT become 4*ceiling(x/4) - 3
    expected = 4 * sympy.ceiling(x/4 - sympy.Rational(3, 4))
    
    # Check that the simplified form matches the expected form
    # This will fail if simplify transforms it to 4*ceiling(x/4) - 3
    assert simplified == expected, f"Expected {expected}, but got {simplified}"