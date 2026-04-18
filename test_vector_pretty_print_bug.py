import pytest
from sympy import *
from sympy.vector import CoordSys3D, Del
from sympy.printing.pretty import pretty

def test_issue_reproduction():
    """Test that vector expressions are properly formatted in pretty print."""
    # Set up coordinate system and variables
    C = CoordSys3D('C')
    t = symbols('t')
    
    # Create a vector expression that should trigger the formatting bug
    # This mimics the type of expression mentioned in the issue
    expr = 2*sin(C.y/5)*C.i*cos(10*t)
    
    # Get the pretty printed output
    result = pretty(expr)
    
    # The bug causes unit vectors to be inserted in the middle of expressions
    # Check that the unit vector 'i_C' appears at the end, not in the middle
    lines = result.split('\n')
    
    # Find lines that contain mathematical content (not just whitespace)
    content_lines = [line for line in lines if line.strip()]
    
    # The issue is that 'i_C' appears in the middle of the expression
    # instead of at the proper position. We expect it NOT to be jumbled.
    # This test will fail on buggy code where formatting is incorrect.
    
    # Check that the output doesn't have the unit vector appearing 
    # in the middle of other mathematical expressions
    for line in content_lines:
        if 'i_C' in line:
            # If i_C appears, it shouldn't be surrounded by other math symbols
            # in a way that indicates it's inserted in the middle
            parts_before_i = line.split('i_C')[0]
            parts_after_i = line.split('i_C')[1] if 'i_C' in line else ''
            
            # The bug manifests as i_C appearing between other mathematical
            # expressions like "expr i_C⋅other_expr" instead of proper formatting
            if parts_before_i.strip().endswith('⋅') and parts_after_i.strip().startswith('⋅'):
                pytest.fail(f"Unit vector i_C appears to be improperly inserted in the middle of expression: {line}")
    
    # Additional check: ensure the expression structure is maintained
    # The pretty print should not have fragmented mathematical expressions
    full_result = ''.join(content_lines)
    
    # Check for the specific pattern mentioned in the issue where
    # mathematical expressions get split incorrectly
    if 'i_C⋅cos' in full_result and '⋅sin' in full_result:
        # This indicates the formatting bug where parts are incorrectly positioned
        pytest.fail("Vector expression formatting is jumbled - unit vector inserted incorrectly")