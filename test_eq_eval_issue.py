import sympy

def test_issue_reproduction():
    """Test that sympy's __eq__ method doesn't eval arbitrary reprs."""
    
    class C:
        def __repr__(self):
            return "Symbol('x').y"
    
    # This should not raise an AttributeError due to eval() being called
    # on the repr "Symbol('x').y" which is invalid Python syntax
    c = C()
    x = sympy.Symbol('x')
    
    # The comparison should not crash with AttributeError
    result = (x == c)
    
    # The result should be False (or NotImplemented), not an exception
    assert result is False or result is NotImplemented