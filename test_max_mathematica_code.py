from sympy import symbols, Max
from sympy.printing.mathematica import mathematica_code

def test_issue_reproduction():
    x = symbols('x')
    result = mathematica_code(Max(x, 2))
    expected = 'Max[x, 2]'
    assert result == expected, f"Expected '{expected}' but got '{result}'"