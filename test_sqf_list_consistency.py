from sympy import symbols, sqf_list

def test_issue_reproduction():
    x = symbols('x')
    
    # Test the problematic case from the issue
    expr = (x**2 + 1) * (x - 1)**2 * (x - 2)**3 * (x - 3)**3
    result = sqf_list(expr)
    
    # Extract the factors list (second element of the tuple)
    factors = result[1]
    
    # Check that factors with the same multiplicity are combined
    # We should have (x**2 - 5*x + 6, 3) instead of separate (x-2,3) and (x-3,3)
    multiplicities = [mult for _, mult in factors]
    
    # Count occurrences of each multiplicity
    mult_counts = {}
    for mult in multiplicities:
        mult_counts[mult] = mult_counts.get(mult, 0) + 1
    
    # The issue is that multiplicity 3 appears twice (for x-2 and x-3)
    # but it should appear only once with the combined factor
    assert mult_counts.get(3, 0) == 1, f"Expected multiplicity 3 to appear once, but got {mult_counts.get(3, 0)} times. Factors: {factors}"