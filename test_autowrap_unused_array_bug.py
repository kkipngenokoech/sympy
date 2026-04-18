import pytest
from sympy.utilities.autowrap import autowrap
from sympy import MatrixSymbol
import numpy as np

def test_issue_reproduction():
    """Test that autowrap with cython backend handles unused array arguments correctly."""
    # Create a MatrixSymbol that won't appear in the expression
    x = MatrixSymbol('x', 2, 1)
    
    # Create an expression that doesn't use x at all
    expr = 1.0
    
    # This should work but currently fails with TypeError
    f = autowrap(expr, backend='cython', args=[x])
    
    # Test with a numpy array
    test_array = np.array([[1.0], [2.0]])
    result = f(test_array)
    
    # Should return 1.0
    assert result == 1.0