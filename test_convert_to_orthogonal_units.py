from sympy.physics.units import joule, second, convert_to

def test_issue_reproduction():
    # Test that convert_to handles orthogonal units properly
    # joule*second cannot be converted to joule since they have different dimensions
    # Current buggy behavior returns joule**(7/9) which is nonsensical
    result = convert_to(joule*second, joule)
    
    # The result should NOT be joule**(7/9) - this is the bug
    # It should either return the original expression or raise an error
    # But currently it returns the nonsensical joule**(7/9)
    assert result != joule**(7/9), f"Expected convert_to to handle orthogonal units properly, but got {result}"