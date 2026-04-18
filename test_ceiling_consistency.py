import sympy
from sympy import symbols, ceiling, sympify

def test_ceiling_consistency():
    """Test that ceiling simplification is consistent with evaluate=False"""
    x = symbols('x')
    
    # Test the reported issue
    expr_str = '4*ceiling(x/4 - 3/4)'
    
    # Parse with evaluate=False
    parsed_expr = sympify(expr_str, evaluate=False)
    simplified_expr = parsed_expr.simplify()
    
    # The simplified expression should maintain the original structure
    # when evaluate=False was used during parsing
    expected = 4*ceiling(x/4 - sympy.Rational(3, 4))
    
    print(f"Original string: {expr_str}")
    print(f"Parsed with evaluate=False: {parsed_expr}")
    print(f"After simplify(): {simplified_expr}")
    print(f"Expected: {expected}")
    
    # The issue is that simplify() should not transform the ceiling expression
    # when the original parsing was done with evaluate=False
    assert str(simplified_expr) == str(expected) or str(simplified_expr) == str(parsed_expr)

if __name__ == "__main__":
    test_ceiling_consistency()
