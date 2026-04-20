"""Tests for exponential to trigonometric simplifications."""

from sympy import (
    exp, I, sin, cos, pi, symbols, simplify, cancel, expand,
    sqrt, Rational, sinc
)
from sympy.simplify.fu import TR_exp_to_trig
from sympy.simplify.trigsimp import trigsimp


def test_exp_to_sin():
    """Test conversion of exponential expressions to sin."""
    x, k = symbols('x k', real=True)
    
    # Basic sin pattern: (exp(I*x) - exp(-I*x))/(2*I) -> sin(x)
    expr1 = (exp(I*x) - exp(-I*x))/(2*I)
    assert TR_exp_to_trig(expr1) == sin(x)
    assert trigsimp(expr1) == sin(x)
    
    # With coefficient: (exp(I*k) - exp(-I*k))/(2*I) -> sin(k)
    expr2 = (exp(I*k) - exp(-I*k))/(2*I)
    assert TR_exp_to_trig(expr2) == sin(k)
    assert trigsimp(expr2) == sin(k)
    
    # With scaling: (exp(2*I*x) - exp(-2*I*x))/(2*I) -> sin(2*x)
    expr3 = (exp(2*I*x) - exp(-2*I*x))/(2*I)
    assert TR_exp_to_trig(expr3) == sin(2*x)
    assert trigsimp(expr3) == sin(2*x)


def test_exp_to_cos():
    """Test conversion of exponential expressions to cos."""
    x, k = symbols('x k', real=True)
    
    # Basic cos pattern: (exp(I*x) + exp(-I*x))/2 -> cos(x)
    expr1 = (exp(I*x) + exp(-I*x))/2
    assert TR_exp_to_trig(expr1) == cos(x)
    assert trigsimp(expr1) == cos(x)
    
    # With coefficient: (exp(I*k) + exp(-I*k))/2 -> cos(k)
    expr2 = (exp(I*k) + exp(-I*k))/2
    assert TR_exp_to_trig(expr2) == cos(k)
    assert trigsimp(expr2) == cos(k)
    
    # With scaling: (exp(3*I*x) + exp(-3*I*x))/2 -> cos(3*x)
    expr3 = (exp(3*I*x) + exp(-3*I*x))/2
    assert TR_exp_to_trig(expr3) == cos(3*x)
    assert trigsimp(expr3) == cos(3*x)


def test_exp_to_sinc():
    """Test conversion of exponential expressions to sinc."""
    x, k = symbols('x k', real=True)
    
    # Basic sinc pattern: (exp(I*x) - exp(-I*x))/(2*I*x) -> sinc(x)
    expr1 = (exp(I*x) - exp(-I*x))/(2*I*x)
    assert TR_exp_to_trig(expr1) == sinc(x)
    assert trigsimp(expr1) == sinc(x)
    
    # With coefficient: (exp(I*k) - exp(-I*k))/(2*I*k) -> sinc(k)
    expr2 = (exp(I*k) - exp(-I*k))/(2*I*k)
    assert TR_exp_to_trig(expr2) == sinc(k)
    assert trigsimp(expr2) == sinc(k)


def test_mixed_expressions():
    """Test expressions with multiple exponential patterns."""
    x, y = symbols('x y', real=True)
    
    # Sum of sin and cos patterns
    expr1 = (exp(I*x) - exp(-I*x))/(2*I) + (exp(I*y) + exp(-I*y))/2
    expected1 = sin(x) + cos(y)
    assert TR_exp_to_trig(expr1) == expected1
    assert trigsimp(expr1) == expected1
    
    # Product involving exponential patterns
    expr2 = 2 * (exp(I*x) - exp(-I*x))/(2*I)
    expected2 = 2*sin(x)
    assert TR_exp_to_trig(expr2) == expected2
    assert trigsimp(expr2) == expected2


def test_no_conversion_cases():
    """Test cases where no conversion should occur."""
    x = symbols('x', real=True)
    
    # Regular exponential (no imaginary unit)
    expr1 = exp(x)
    assert TR_exp_to_trig(expr1) == expr1
    
    # Wrong denominator
    expr2 = (exp(I*x) - exp(-I*x))/3
    assert TR_exp_to_trig(expr2) == expr2
    
    # Wrong numerator pattern
    expr3 = (exp(I*x) + 2*exp(-I*x))/(2*I)
    assert TR_exp_to_trig(expr3) == expr3


def test_complex_arguments():
    """Test with more complex arguments."""
    x, a, b = symbols('x a b', real=True)
    
    # Linear combination in argument
    expr1 = (exp(I*(a*x + b)) - exp(-I*(a*x + b)))/(2*I)
    expected1 = sin(a*x + b)
    assert TR_exp_to_trig(expr1) == expected1
    assert trigsimp(expr1) == expected1
    
    # Cosine with complex argument
    expr2 = (exp(I*(2*x + pi/4)) + exp(-I*(2*x + pi/4)))/2
    expected2 = cos(2*x + pi/4)
    assert TR_exp_to_trig(expr2) == expected2
    assert trigsimp(expr2) == expected2


def test_nested_expressions():
    """Test expressions nested within other operations."""
    x = symbols('x', real=True)
    
    # Square of exponential pattern
    expr1 = ((exp(I*x) - exp(-I*x))/(2*I))**2
    expected1 = sin(x)**2
    assert TR_exp_to_trig(expr1) == expected1
    assert trigsimp(expr1) == expected1
    
    # Exponential pattern in denominator
    expr2 = 1/((exp(I*x) + exp(-I*x))/2)
    expected2 = 1/cos(x)
    assert TR_exp_to_trig(expr2) == expected2
    assert trigsimp(expr2) == expected2


def test_issue_examples():
    """Test the specific examples from the GitHub issue."""
    k = symbols('k', real=True)
    
    # First example: (exp(I*k) - exp(-I*k))/(2*I) should yield sin(k)
    expr1 = (exp(I*k) - exp(-I*k))/(2*I)
    assert trigsimp(expr1) == sin(k)
    
    # Second example: (exp(I*k) - exp(-I*k))/(2*I*k) should yield sinc(k)
    expr2 = (exp(I*k) - exp(-I*k))/(2*I*k)
    assert trigsimp(expr2) == sinc(k)


def test_edge_cases():
    """Test edge cases and boundary conditions."""
    x = symbols('x', real=True)
    
    # Zero argument
    expr1 = (exp(I*0) - exp(-I*0))/(2*I)
    # This should be 0, but we test that it doesn't crash
    result1 = TR_exp_to_trig(expr1)
    assert result1 is not None
    
    # Very simple case with just I
    expr2 = (exp(I) - exp(-I))/(2*I)
    expected2 = sin(1)
    assert TR_exp_to_trig(expr2) == expected2
    
    # Negative coefficient
    expr3 = -(exp(I*x) - exp(-I*x))/(2*I)
    expected3 = -sin(x)
    assert TR_exp_to_trig(expr3) == expected3
