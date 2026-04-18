import inspect
from sympy import lambdify

def test_issue_reproduction():
    # Test single-element tuple - this should have a trailing comma
    func = lambdify([], tuple([1]))
    source = inspect.getsource(func)
    
    # The generated code should contain "return (1,)" not "return (1)"
    # This assertion will FAIL on the buggy code because it generates (1) instead of (1,)
    assert "return (1,)" in source, f"Expected 'return (1,)' but got: {source}"
    
    # Verify the function actually returns a tuple, not an integer
    result = func()
    assert isinstance(result, tuple), f"Expected tuple but got {type(result)}: {result}"
    assert len(result) == 1, f"Expected single-element tuple but got length {len(result)}"
    assert result[0] == 1, f"Expected first element to be 1 but got {result[0]}"