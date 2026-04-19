import pytest
from sympy import symbols, exp, I, trigsimp, sin, simplify
from sympy.abc import k

def test_issue_reproduction():
    # Test the main case from the issue
    f = 1 / 2 * (-I*exp(I*k) + I*exp(-I*k))
    result = trigsimp(f)
    expected = sin(k)
    
    # The test should fail because trigsimp doesn't currently handle exp->trig conversion
    # We check that the result is NOT simplified to sin(k)
    assert result != expected, f"Expected trigsimp to fail, but got {result} == {expected}"
    
    # Verify that the expressions are actually mathematically equivalent
    # (this should pass to confirm our test setup is correct)
    difference = simplify(f - expected)
    assert difference == 0, f"Mathematical equivalence check failed: {difference}"
    
    # The actual assertion that should fail on current code but pass after fix
    assert result == expected, f"trigsimp({f}) should equal {expected}, but got {result}"