import sympy as sp

def test_issue_reproduction():
    # This should work without evaluate(False)
    result1 = sp.S('Point2D(Integer(1),Integer(2))')
    assert str(result1) == 'Point2D(1, 2)'
    
    # This should also work with explicit evaluate=False
    result2 = sp.S('Point2D(Integer(1),Integer(2))', evaluate=False)
    assert str(result2) == 'Point2D(1, 2)'
    
    # This should work but currently fails with "Imaginary coordinates are not permitted."
    with sp.evaluate(False):
        result3 = sp.S('Point2D(Integer(1),Integer(2))')
        assert str(result3) == 'Point2D(1, 2)'