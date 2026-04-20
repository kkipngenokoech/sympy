import pytest
from sympy import Matrix

def test_issue_reproduction():
    """Test that @ operator should fail when one operand is not a matrix."""
    A = Matrix([[1, 2], [3, 4]])
    scalar = 5
    
    # This should raise ValueError like NumPy does, but currently doesn't
    with pytest.raises(ValueError, match="Scalar operands are not allowed, use '\*' instead"):
        result = A @ scalar
    
    # Also test the reverse case
    with pytest.raises(ValueError, match="Scalar operands are not allowed, use '\*' instead"):
        result = scalar @ A