from sympy import acsc, asec, latex, Symbol

def test_issue_reproduction():
    x = Symbol('x')
    
    # Test acsc with full inverse trig style
    result_acsc = latex(acsc(x), inv_trig_style="full")
    expected_acsc = r'\operatorname{arccsc}{\left (x \right )}'
    
    # Test asec with full inverse trig style
    result_asec = latex(asec(x), inv_trig_style="full")
    expected_asec = r'\operatorname{arcsec}{\left (x \right )}'
    
    # These assertions will fail because acsc and asec are not in inv_trig_table
    assert result_acsc == expected_acsc, f"Expected {expected_acsc}, got {result_acsc}"
    assert result_asec == expected_asec, f"Expected {expected_asec}, got {result_asec}"