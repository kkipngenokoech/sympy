from sympy.physics.units import milli, W

def test_issue_reproduction():
    result = milli * W
    # The bug: milli*W evaluates to 1 instead of a proper unit expression
    # This assertion will fail because result == 1 on the buggy code
    assert result != 1, f"milli*W should not evaluate to 1, got {result}"
    # Additional check: the result should represent milliwatts
    assert hasattr(result, 'scale_factor') or str(result) != '1', f"Expected a unit expression, got {result}"