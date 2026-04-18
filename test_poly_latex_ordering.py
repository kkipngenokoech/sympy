from sympy import symbols, Poly
from sympy.printing.latex import latex
from sympy.printing.pretty import pretty

def test_poly_latex_ordering():
    """Test that LaTeX printer uses same monomial ordering as str and pretty printers."""
    a, b, c, x = symbols('a b c x')
    p = Poly([a, 1, b, 2, c, 3], x)
    
    # Get string representations
    str_repr = str(p)
    pretty_repr = pretty(p)
    latex_repr = latex(p)
    
    print("String representation:", str_repr)
    print("Pretty representation:", pretty_repr)
    print("LaTeX representation:", latex_repr)
    
    # The issue is that LaTeX doesn't follow the same ordering
    # We need to verify the ordering is consistent
    
if __name__ == "__main__":
    test_poly_latex_ordering()
