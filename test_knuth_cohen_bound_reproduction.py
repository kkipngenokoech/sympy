from sympy.polys import ring, ZZ
from sympy.polys.factortools import dup_zz_mignotte_bound, dmp_zz_mignotte_bound

def test_issue_reproduction():
    """Test that Knuth-Cohen bound should be used instead of Mignotte bound."""
    R, x = ring("x", ZZ)
    
    # Test polynomial: x^4 + 2*x^3 + 3*x^2 + 4*x + 5
    f = [1, 2, 3, 4, 5]  # coefficients in dense representation
    
    # Current Mignotte bound
    current_bound = dup_zz_mignotte_bound(f, ZZ)
    
    # Expected Knuth-Cohen bound should be smaller
    # For this polynomial, Knuth-Cohen bound should be approximately 12
    # while Mignotte bound is much larger
    expected_knuth_cohen_bound = 12
    
    # This assertion should fail with current Mignotte implementation
    # because Mignotte bound is typically much larger than Knuth-Cohen
    assert current_bound <= expected_knuth_cohen_bound, f"Expected Knuth-Cohen bound <= {expected_knuth_cohen_bound}, got Mignotte bound {current_bound}"
    
    # Test multivariate case
    R, x, y = ring("x,y", ZZ)
    f_multi = [[1, 2], [3, 4]]  # represents x*y + 2*x + 3*y + 4
    
    current_bound_multi = dmp_zz_mignotte_bound(f_multi, 1, ZZ)
    expected_knuth_cohen_bound_multi = 8
    
    # This should also fail with current implementation
    assert current_bound_multi <= expected_knuth_cohen_bound_multi, f"Expected multivariate Knuth-Cohen bound <= {expected_knuth_cohen_bound_multi}, got Mignotte bound {current_bound_multi}"