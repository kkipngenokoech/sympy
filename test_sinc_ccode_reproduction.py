from sympy import symbols, sinc, ccode

def test_issue_reproduction():
    x = symbols('x')
    expr = sinc(x)
    # This should generate C code like "sin(x)/x" but currently fails
    result = ccode(expr)
    # The test expects some valid C code representation, not an error
    assert 'sin' in result and 'x' in result