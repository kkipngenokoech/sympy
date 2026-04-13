import pytest
from sympy import symbols, sinc
from sympy.printing.ccode import ccode

def test_issue_reproduction():
    x = symbols('x')
    # This should work but currently fails because sinc is not in known_functions
    result = ccode(sinc(x))
    # The expected output should be a conditional expression since math.h doesn't have sinc
    # It should generate something like: ((x) != 0 ? sin(x)/(x) : 1)
    assert 'sinc' not in result  # Should not contain the raw function name
    assert 'sin(' in result     # Should contain sin function
    assert '?' in result        # Should be a conditional expression