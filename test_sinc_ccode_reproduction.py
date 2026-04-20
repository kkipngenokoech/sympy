from sympy import symbols, sinc, ccode

def test_issue_reproduction():
    x = symbols('x')
    # This should generate valid C code for sinc(x)
    # Currently fails because there's no C code printer for sinc
    result = ccode(sinc(x))
    # The test expects some valid C code output, not an error
    assert isinstance(result, str) and len(result) > 0