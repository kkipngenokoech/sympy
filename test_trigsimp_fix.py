#!/usr/bin/env python3
"""
Test cases for the trigsimp fix for sqrt(sin(x)**2) with complex variables.
"""

from sympy import *
from sympy.abc import x, y

def test_sqrt_sin_squared_complex():
    """Test that sqrt(sin(x)**2) is not simplified to sin(x) for complex x."""
    # For general complex x, sqrt(sin(x)**2) should be |sin(x)|, not sin(x)
    expr = cos(x) + sqrt(sin(x)**2)
    result = trigsimp(expr)
    
    # The result should be cos(x) + Abs(sin(x)) for complex x
    expected = cos(x) + Abs(sin(x))
    
    print(f"Original expression: {expr}")
    print(f"Trigsimp result: {result}")
    print(f"Expected: {expected}")
    
    # Check that it's not incorrectly simplified to cos(x) + sin(x)
    incorrect = cos(x) + sin(x)
    assert result != incorrect, f"trigsimp incorrectly simplified to {incorrect}"
    
    # For the fix, we expect it to remain as sqrt(sin(x)**2) or become Abs(sin(x))
    # since we can't assume x is real
    assert result == expected or result == expr

def test_sqrt_sin_squared_real():
    """Test that sqrt(sin(x)**2) can be simplified when x is known to be real."""
    x_real = symbols('x', real=True)
    expr = cos(x_real) + sqrt(sin(x_real)**2)
    result = trigsimp(expr)
    
    print(f"\nReal case - Original expression: {expr}")
    print(f"Real case - Trigsimp result: {result}")
    
    # For real x, sqrt(sin(x)**2) = |sin(x)|
    expected = cos(x_real) + Abs(sin(x_real))
    assert result == expected or result == expr

def test_other_trig_functions():
    """Test sqrt(trig_func(x)**2) for other trig functions."""
    test_cases = [
        sqrt(cos(x)**2),
        sqrt(tan(x)**2),
        sqrt(cot(x)**2),
    ]
    
    for expr in test_cases:
        result = trigsimp(expr)
        print(f"\nExpression: {expr}")
        print(f"Result: {result}")
        
        # Should not be simplified to just the trig function for complex x
        trig_func = expr.args[0].base
        assert result != trig_func, f"Incorrectly simplified {expr} to {trig_func}"

def test_nested_expressions():
    """Test more complex expressions containing sqrt(sin(x)**2)."""
    expr1 = sin(x) * sqrt(cos(x)**2) + cos(x)
    expr2 = sqrt(sin(x)**2) + sqrt(cos(x)**2)
    
    result1 = trigsimp(expr1)
    result2 = trigsimp(expr2)
    
    print(f"\nNested 1 - Original: {expr1}")
    print(f"Nested 1 - Result: {result1}")
    
    print(f"\nNested 2 - Original: {expr2}")
    print(f"Nested 2 - Result: {result2}")
    
    # These should not be simplified incorrectly
    assert result1 != sin(x) * cos(x) + cos(x)
    assert result2 != sin(x) + cos(x)

if __name__ == "__main__":
    print("Testing trigsimp fix for sqrt(sin(x)**2) with complex variables...")
    
    test_sqrt_sin_squared_complex()
    test_sqrt_sin_squared_real()
    test_other_trig_functions()
    test_nested_expressions()
    
    print("\nAll tests completed!")
