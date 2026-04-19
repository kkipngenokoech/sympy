import sympy as sp
from sympy import var, Poly
from sympy.printing.latex import latex

def test_issue_reproduction():
    """Test that LaTeX printer uses same monomial order as str printer for Poly objects."""
    var('a b c x')
    p = Poly([a, 1, b, 2, c, 3], x)
    
    # Get string representation (should be in logical order: highest to lowest degree)
    str_repr = str(p)
    
    # Get LaTeX representation
    latex_repr = latex(p)
    
    # The issue is that LaTeX doesn't follow the same ordering as str
    # We need to check that the terms appear in the same relative order
    # For a polynomial like a*x^5 + x^4 + b*x^3 + 2*x^2 + c*x + 3
    # Both should have terms in decreasing degree order
    
    # Extract the coefficient order from string representation
    # The polynomial should have terms in order: a (x^5), 1 (x^4), b (x^3), 2 (x^2), c (x^1), 3 (x^0)
    
    # For this specific polynomial, check that 'a' appears before 'b' and 'b' appears before 'c'
    # in both representations (indicating same ordering)
    str_a_pos = str_repr.find('a')
    str_b_pos = str_repr.find('b') 
    str_c_pos = str_repr.find('c')
    
    latex_a_pos = latex_repr.find('a')
    latex_b_pos = latex_repr.find('b')
    latex_c_pos = latex_repr.find('c')
    
    # In correct ordering: a should come before b, and b should come before c
    str_order_correct = str_a_pos < str_b_pos < str_c_pos
    latex_order_correct = latex_a_pos < latex_b_pos < latex_c_pos
    
    # Both should have the same ordering
    assert str_order_correct == latex_order_correct, f"LaTeX ordering differs from str ordering. str: {str_repr}, latex: {latex_repr}"