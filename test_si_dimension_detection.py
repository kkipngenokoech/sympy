import pytest
from sympy import exp, symbols
from sympy.physics import units
from sympy.physics.units.systems import SI

def test_issue_reproduction():
    # Test that SI._collect_factor_and_dimension() properly detects
    # that exponents must be dimensionless
    x = symbols('x')
    
    # Create an expression with a dimensional quantity in the exponent
    # This should raise an error or be detected as invalid since
    # exponents must be dimensionless
    dimensional_expr = exp(units.meter)
    
    # The method should detect that the exponent has dimensions
    # and either raise an error or handle it appropriately
    try:
        factor, dimension = SI._collect_factor_and_dimension(dimensional_expr)
        # If we get here without error, the bug exists - 
        # the method failed to detect the dimensional exponent
        assert False, "Expected error for dimensional exponent but got none"
    except (ValueError, TypeError, AttributeError) as e:
        # This is the expected behavior - dimensional exponents should be rejected
        pass