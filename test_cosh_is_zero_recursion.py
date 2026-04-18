from sympy import sympify

def test_issue_reproduction():
    """Test that cosh.is_zero doesn't cause recursion error."""
    expr = sympify("cosh(acos(-i + acosh(-g + i)))")
    # This should not raise RecursionError
    result = expr.is_zero
    # cosh is never zero for finite arguments, so this should be False
    assert result is False