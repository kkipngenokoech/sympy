from sympy import symbols, sinc
from sympy.printing.ccode import ccode

def test_issue_reproduction():
    x = symbols('x')
    result = ccode(sinc(x))
    # The current buggy behavior returns a comment indicating it's not supported
    # This test will fail because we expect proper C code, not a comment
    assert '// Not supported in C:' not in result
    assert 'sinc(x)' not in result  # Should not contain the original function name
    # Should contain the mathematical definition instead
    assert 'sin(' in result and '!= 0' in result