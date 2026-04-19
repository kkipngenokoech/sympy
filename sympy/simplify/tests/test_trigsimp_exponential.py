from sympy import *
from sympy.functions.elementary.trigonometric import exp_to_trig
from sympy.functions.elementary.miscellaneous import sinc


def test_exp_to_sin():
    """Test conversion of exponential expressions to sin."""
    x, k = symbols('x k')
    I = S.ImaginaryUnit
    
    # Basic sin pattern
    expr = (exp(I*k) - exp(-I*k))/(2*I)
    result = exp_to_trig(expr)
    assert result == sin(k)
    
    # With different variable
    expr = (exp(I*x) - exp(-I*x))/(2*I)
    result = exp_to_trig(expr)
    assert result == sin(x)
    
    # With coefficient
    expr = (exp(2*I*k) - exp(-2*I*k))/(2*I)
    result = exp_to_trig(expr)
    assert result == sin(2*k)


def test_exp_to_cos():
    """Test conversion of exponential expressions to cos."""
    x, k = symbols('x k')
    I = S.ImaginaryUnit
    
    # Basic cos pattern
    expr = (exp(I*k) + exp(-I*k))/2
    result = exp_to_trig(expr)
    assert result == cos(k)
    
    # With different variable
    expr = (exp(I*x) + exp(-I*x))/2
    result = exp_to_trig(expr)
    assert result == cos(x)
    
    # With coefficient
    expr = (exp(3*I*k) + exp(-3*I*k))/2
    result = exp_to_trig(expr)
    assert result == cos(3*k)


def test_sin_over_x_to_sinc():
    """Test conversion of sin(x)/x to sinc(x)."""
    x, k = symbols('x k')
    
    # Basic sinc pattern
    expr = sin(k)/k
    result = exp_to_trig(expr)
    assert result == sinc(k)
    
    # With different variable
    expr = sin(x)/x
    result = exp_to_trig(expr)
    assert result == sinc(x)
    
    # With coefficient in argument
    expr = sin(2*k)/(2*k)
    result = exp_to_trig(expr)
    assert result == sinc(2*k)


def test_no_conversion():
    """Test that expressions that don't match patterns are unchanged."""
    x, k = symbols('x k')
    I = S.ImaginaryUnit
    
    # Random expression
    expr = x**2 + 1
    result = exp_to_trig(expr)
    assert result == expr
    
    # Wrong denominator for sin
    expr = (exp(I*k) - exp(-I*k))/3
    result = exp_to_trig(expr)
    assert result == expr
    
    # Wrong denominator for cos
    expr = (exp(I*k) + exp(-I*k))/3
    result = exp_to_trig(expr)
    assert result == expr
    
    # Wrong numerator pattern
    expr = (exp(I*k) + 2*exp(-I*k))/(2*I)
    result = exp_to_trig(expr)
    assert result == expr


def test_complex_expressions():
    """Test more complex expressions with multiple terms."""
    x, k = symbols('x k')
    I = S.ImaginaryUnit
    
    # Expression that should simplify to sin
    expr1 = (exp(I*k) - exp(-I*k))/(2*I)
    # Expression that should simplify to cos  
    expr2 = (exp(I*k) + exp(-I*k))/2
    
    # Combined expression
    combined = expr1 + expr2
    result1 = exp_to_trig(expr1)
    result2 = exp_to_trig(expr2)
    
    assert result1 == sin(k)
    assert result2 == cos(k)


def test_edge_cases():
    """Test edge cases and boundary conditions."""
    x, k = symbols('x k')
    I = S.ImaginaryUnit
    
    # Zero case
    expr = S.Zero
    result = exp_to_trig(expr)
    assert result == S.Zero
    
    # Simple exponential (no pattern match)
    expr = exp(I*k)
    result = exp_to_trig(expr)
    assert result == expr
    
    # Single term (no pattern match)
    expr = exp(I*k)/(2*I)
    result = exp_to_trig(expr)
    assert result == expr


def test_integration_with_simplify():
    """Test that the function works well with SymPy's simplify."""
    x, k = symbols('x k')
    I = S.ImaginaryUnit
    
    # Test that we can use exp_to_trig in a simplification pipeline
    expr = (exp(I*k) - exp(-I*k))/(2*I)
    simplified = simplify(exp_to_trig(expr))
    assert simplified == sin(k)
    
    # Test with expand
    expr = (exp(I*k) + exp(-I*k))/2
    expanded = expand(exp_to_trig(expr))
    assert expanded == cos(k)
