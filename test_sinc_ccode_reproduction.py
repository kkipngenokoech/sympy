import pytest
from sympy import symbols, sinc, ccode

def test_issue_reproduction():
    x = symbols('x')
    result = ccode(sinc(x))
    # The current buggy behavior returns a comment indicating it's not supported
    # This test will fail because we expect proper C code, not a comment
    assert '// Not supported in C:' not in result
    assert 'sinc(x)' not in result  # Should not contain the original function name
    # Should contain conditional logic for sinc implementation
    assert '?' in result or 'if' in result  # Should have conditional structure