from sympy import *
from sympy.core.cache import clear_cache
import pytest

def test_subs_with_hyperbolic_piecewise():
    """Test that subs() works correctly with hyperbolic functions containing piecewise arguments."""
    
    # Clear cache to ensure clean state
    clear_cache()
    
    # Define symbols
    z = Symbol('z', real=True)
    
    # Create the problematic expression from the issue
    # This is the minimal working example that triggers the PolynomialError
    expr = cosh(Piecewise((0, Eq(z, 0)), (z, True))) / z
    
    # This should not raise a PolynomialError
    try:
        result = expr.subs(1, 1.0)
        # If we get here, the substitution worked
        assert True
    except Exception as e:
        # Print the error for debugging
        print(f"Error occurred: {type(e).__name__}: {e}")
        # Re-raise to fail the test
        raise

def test_subs_with_tanh_piecewise():
    """Test that subs() works correctly with tanh functions containing piecewise arguments."""
    
    # Clear cache to ensure clean state
    clear_cache()
    
    # Define symbols
    z = Symbol('z', real=True)
    
    # Test with tanh as mentioned in the issue
    expr = tanh(Piecewise((0, Eq(z, 0)), (z, True))) / z
    
    # This should not raise a PolynomialError
    try:
        result = expr.subs(1, 1.0)
        # If we get here, the substitution worked
        assert True
    except Exception as e:
        # Print the error for debugging
        print(f"Error occurred: {type(e).__name__}: {e}")
        # Re-raise to fail the test
        raise

def test_subs_with_sinh_piecewise():
    """Test that subs() works correctly with sinh functions containing piecewise arguments.
    
    According to the issue, sinh should work fine, so this is a control test.
    """
    
    # Clear cache to ensure clean state
    clear_cache()
    
    # Define symbols
    z = Symbol('z', real=True)
    
    # Test with sinh - this should work according to the issue
    expr = sinh(Piecewise((0, Eq(z, 0)), (z, True))) / z
    
    # This should work without issues
    result = expr.subs(1, 1.0)
    assert result is not None

def test_complex_expression_with_exp():
    """Test a more complex expression similar to what might be used in practice."""
    
    # Clear cache to ensure clean state
    clear_cache()
    
    # Define symbols
    z = Symbol('z', real=True)
    
    # More complex expression that might trigger the issue
    expr = exp(cosh(Piecewise((0, Eq(z, 0)), (z, True)))) / z
    
    # This should not raise a PolynomialError
    try:
        result = expr.subs(1, 1.0)
        # If we get here, the substitution worked
        assert True
    except Exception as e:
        # Print the error for debugging
        print(f"Error occurred: {type(e).__name__}: {e}")
        # Re-raise to fail the test
        raise

def test_int_to_float_substitution():
    """Test the specific use case mentioned in the issue: casting int to float."""
    
    # Clear cache to ensure clean state
    clear_cache()
    
    # Define symbols
    z = Symbol('z', real=True)
    
    # Create expression with integer constants
    expr = cosh(Piecewise((0, Eq(z, 0)), (z, True))) / z + 1
    
    # Try to substitute all integer atoms with float equivalents
    # This is the umbrella-casting mentioned in the issue
    try:
        # Find all integer atoms and substitute them with floats
        int_atoms = expr.atoms(Integer)
        subs_dict = {atom: float(atom) for atom in int_atoms}
        result = expr.subs(subs_dict)
        assert result is not None
    except Exception as e:
        # Print the error for debugging
        print(f"Error occurred during int->float substitution: {type(e).__name__}: {e}")
        # Re-raise to fail the test
        raise

if __name__ == "__main__":
    # Run the tests to see which ones fail
    test_functions = [
        test_subs_with_hyperbolic_piecewise,
        test_subs_with_tanh_piecewise,
        test_subs_with_sinh_piecewise,
        test_complex_expression_with_exp,
        test_int_to_float_substitution
    ]
    
    for test_func in test_functions:
        try:
            print(f"Running {test_func.__name__}...")
            test_func()
            print(f"✓ {test_func.__name__} passed")
        except Exception as e:
            print(f"✗ {test_func.__name__} failed: {type(e).__name__}: {e}")
            import traceback
            traceback.print_exc()
            print()
