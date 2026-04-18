import pytest
from sympy import symbols, I, exp, trigsimp, sin, simplify
from sympy.abc import k

def test_issue_reproduction():
    # Test the main case from the issue
    f = 1 / 2 * (-I*exp(I*k) + I*exp(-I*k))
    result = trigsimp(f)
    expected = sin(k)
    
    # The test should fail because trigsimp doesn't currently recognize this pattern
    # We expect the result to be sin(k), but it will remain unsimplified
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Also test that the expressions are mathematically equivalent
    # This should pass even if trigsimp fails, confirming the math is correct
    difference = simplify(f - sin(k))
    assert difference == 0, f"Mathematical equivalence check failed: {difference}"