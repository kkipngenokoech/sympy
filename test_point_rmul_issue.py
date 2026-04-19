import sympy
from sympy import geometry as ge

def test_issue_reproduction():
    """Test that Point supports both left and right multiplication with numbers."""
    point1 = ge.Point(1, 2)
    point2 = ge.Point(3, 4)
    
    # This should work (left multiplication: point * number)
    result1 = point1 + point2 * sympy.sympify(2.0)
    
    # This should also work but currently fails (right multiplication: number * point)
    result2 = point1 + sympy.sympify(2.0) * point2
    
    # Both results should be equal
    assert result1 == result2