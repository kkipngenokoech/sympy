import pytest
from sympy.vector import CoordSys3D
from sympy import pprint
from io import StringIO
import sys

def test_issue_reproduction():
    """Test that vector pretty printing works correctly without breaking."""
    C = CoordSys3D('C')
    v = 3*C.i + 4*C.j + 5*C.k
    
    # Capture the output of pprint to check if it breaks
    old_stdout = sys.stdout
    sys.stdout = captured_output = StringIO()
    
    try:
        # This should not raise an exception and should produce proper output
        pprint(v)
        output = captured_output.getvalue()
        
        # The output should not be empty and should contain vector components
        assert output.strip() != "", "Pretty printing produced empty output"
        assert "C.i" in output or "i" in output, "Vector components not found in output"
        
    except Exception as e:
        pytest.fail(f"Pretty printing vectors raised an exception: {e}")
    finally:
        sys.stdout = old_stdout
    
    # Test that the vector has proper pretty printing methods
    # This will fail because vectors lack _pretty methods
    assert hasattr(v, '_pretty'), "Vector should have _pretty method for proper pretty printing"