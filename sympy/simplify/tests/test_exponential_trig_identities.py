from sympy import (
    symbols, I, exp, sin, cos, sinc, trigsimp, simplify, pi, E
)
from sympy.abc import k, x, y, z


def test_exp_to_sin():
    """Test conversion of exponential expressions to sin."""
    # Basic case: (exp(I*k) - exp(-I*k))/(2*I) -> sin(k)
    expr = (exp(I*k) - exp(-I*k))/(2*I)
    result = trigsimp(expr)
    assert result == sin(k)
    
    # With coefficient: (exp(2*I*k) - exp(-2*I*k))/(2*I) -> sin(2*k)
    expr = (exp(2*I*k) - exp(-2*I*k))/(2*I)
    result = trigsimp(expr)
    assert result == sin(2*k)
    
    # Different variable
    expr = (exp(I*x) - exp(-I*x))/(2*I)
    result = trigsimp(expr)
    assert result == sin(x)


def test_exp_to_cos():
    """Test conversion of exponential expressions to cos."""
    # Basic case: (exp(I*k) + exp(-I*k))/2 -> cos(k)
    expr = (exp(I*k) + exp(-I*k))/2
    result = trigsimp(expr)
    assert result == cos(k)
    
    # With coefficient: (exp(3*I*k) + exp(-3*I*k))/2 -> cos(3*k)
    expr = (exp(3*I*k) + exp(-3*I*k))/2
    result = trigsimp(expr)
    assert result == cos(3*k)
    
    # Different variable
    expr = (exp(I*y) + exp(-I*y))/2
    result = trigsimp(expr)
    assert result == cos(y)


def test_exp_to_sinc():
    """Test conversion of exponential expressions to sinc."""
    # Basic case: (exp(I*k) - exp(-I*k))/(2*I*k) -> sinc(k)
    expr = (exp(I*k) - exp(-I*k))/(2*I*k)
    result = trigsimp(expr)
    assert result == sinc(k)
    
    # With coefficient in argument: (exp(2*I*k) - exp(-2*I*k))/(2*I*k) -> sinc(2*k)
    expr = (exp(2*I*k) - exp(-2*I*k))/(2*I*k)
    result = trigsimp(expr)
    assert result == sinc(2*k)
    
    # Different variable
    expr = (exp(I*x) - exp(-I*x))/(2*I*x)
    result = trigsimp(expr)
    assert result == sinc(x)
    
    # With coefficient in denominator: (exp(I*k) - exp(-I*k))/(4*I*k) -> sinc(k)/2
    expr = (exp(I*k) - exp(-I*k))/(4*I*k)
    result = trigsimp(expr)
    assert result == sinc(k)/2


def test_complex_expressions():
    """Test more complex expressions involving exponentials."""
    # Sum of exponential expressions
    expr1 = (exp(I*k) - exp(-I*k))/(2*I)
    expr2 = (exp(I*x) + exp(-I*x))/2
    combined = expr1 + expr2
    result = trigsimp(combined)
    assert result == sin(k) + cos(x)
    
    # Product of exponential expressions
    expr = ((exp(I*k) - exp(-I*k))/(2*I)) * ((exp(I*x) + exp(-I*x))/2)
    result = trigsimp(expr)
    assert result == sin(k)*cos(x)


def test_edge_cases():
    """Test edge cases and expressions that should not be simplified."""
    # Expression that doesn't match patterns should remain unchanged
    expr = exp(k) + exp(-k)
    result = trigsimp(expr)
    assert result == expr
    
    # Expression with real exponentials should remain unchanged
    expr = (exp(k) - exp(-k))/2
    result = trigsimp(expr)
    assert result == expr
    
    # Already trigonometric expressions should work as before
    expr = sin(k)**2 + cos(k)**2
    result = trigsimp(expr)
    assert result == 1


def test_nested_expressions():
    """Test expressions with nested structure."""
    # Exponential inside other functions
    from sympy import log, sqrt
    
    expr = log((exp(I*k) - exp(-I*k))/(2*I))
    result = trigsimp(expr)
    assert result == log(sin(k))
    
    expr = sqrt((exp(I*k) + exp(-I*k))/2)
    result = trigsimp(expr)
    assert result == sqrt(cos(k))


def test_multiple_variables():
    """Test expressions with multiple variables."""
    # Multiple independent exponential terms
    expr = (exp(I*x) - exp(-I*x))/(2*I) + (exp(I*y) + exp(-I*y))/2
    result = trigsimp(expr)
    assert result == sin(x) + cos(y)
    
    # Mixed exponential and trigonometric
    expr = (exp(I*k) - exp(-I*k))/(2*I) + sin(x)*cos(x)
    result = trigsimp(expr)
    # The sin(x)*cos(x) part might be simplified to sin(2*x)/2 depending on method
    # but the exponential part should become sin(k)
    assert result.has(sin(k))


def test_preservation_of_existing_functionality():
    """Ensure existing trigsimp functionality is preserved."""
    # Standard trigonometric simplifications should still work
    expr = sin(x)**2 + cos(x)**2
    result = trigsimp(expr)
    assert result == 1
    
    expr = 2*sin(x)*cos(x)
    result = trigsimp(expr)
    # This might be simplified to sin(2*x) depending on the method
    assert result in [2*sin(x)*cos(x), sin(2*x)]
    
    # Hyperbolic functions should still work
    from sympy import sinh, cosh
    expr = sinh(x)**2 - cosh(x)**2
    result = trigsimp(expr)
    assert result == -1
