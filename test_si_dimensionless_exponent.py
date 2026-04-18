#!/usr/bin/env python3
"""
Test script to reproduce and verify the fix for SI._collect_factor_and_dimension()
not properly detecting dimensionless exponents.
"""

from sympy import exp, pi, E
from sympy.physics import units
from sympy.physics.units.systems import SI

def test_dimensionless_exponent():
    """Test that SI can properly handle dimensionless exponents in exp()."""
    
    # Create a dimensionless quantity
    dimensionless_expr = pi  # pi is dimensionless
    
    # Create an exponential with dimensionless exponent
    expr = exp(dimensionless_expr)
    
    # This should work without error and recognize the exponent as dimensionless
    try:
        factor, dimension = SI._collect_factor_and_dimension(expr)
        print(f"Success: factor={factor}, dimension={dimension}")
        
        # The result should be dimensionless (dimension should be 1)
        assert dimension == 1, f"Expected dimensionless result, got {dimension}"
        print("Test passed: exp(dimensionless) is correctly identified as dimensionless")
        
    except Exception as e:
        print(f"Error: {e}")
        print("Test failed: SI._collect_factor_and_dimension() cannot handle dimensionless exponents")
        raise

if __name__ == "__main__":
    test_dimensionless_exponent()
