from sympy import Mod, S

def test_issue_reproduction():
    # Test that Mod(x**2, x) is not always 0 when x is not an integer
    x = S(1.5)
    result = Mod(x**2, x)
    # When x = 1.5, x**2 = 2.25, and 2.25 % 1.5 = 0.75, not 0
    expected = S(0.75)
    assert result == expected, f"Expected {expected}, but got {result}"