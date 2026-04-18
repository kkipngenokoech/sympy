import pytest
from sympy import symbols, Eq, exp, Function
from sympy.geometry.util import idiff

def test_issue_reproduction():
    x, y = symbols('x y')
    f = Function('f')
    
    # Test 1: idiff should support Eq objects
    # This should work: idiff(Eq(y*exp(y), x*exp(x)), y, x)
    # But currently fails with IndexError: list index out of range
    with pytest.raises((IndexError, ValueError)):
        idiff(Eq(y*exp(y), x*exp(x)), y, x)
    
    # Test 2: idiff should support function notation f(x) instead of just y
    # This should work: idiff(f(x)*exp(f(x)) - x*exp(x), f(x), x)
    # But currently fails with ValueError: expecting x-dependent symbol(s) but got: f(x)
    with pytest.raises(ValueError, match="expecting x-dependent symbol\(s\) but got"):
        idiff(f(x)*exp(f(x)) - x*exp(x), f(x), x)