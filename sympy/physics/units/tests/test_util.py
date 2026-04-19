from sympy.physics.units import (
    meter, kilogram, second, joule, newton, watt, pascal, hertz,
    convert_to, quantity_simplify, check_dimensions
)
from sympy.physics.units.systems import SI
from sympy import symbols, Rational
from sympy.testing.pytest import raises


def test_convert_to():
    # Test basic conversions
    assert convert_to(joule, kilogram*meter**2/second**2) == kilogram*meter**2/second**2
    
    # Test orthogonal units - should return original expression
    result = convert_to(joule*second, joule)
    assert result == joule*second
    
    # Test another orthogonal case
    result = convert_to(meter*kilogram, second)
    assert result == meter*kilogram
    
    # Test valid conversions still work
    assert convert_to(joule*second, joule*second) == joule*second
    assert convert_to(joule*second, kilogram*meter**2/second) == kilogram*meter**2/second
    
    # Test conversion with multiple target units
    result = convert_to(newton, [kilogram, meter, second])
    assert result == kilogram*meter/second**2


def test_quantity_simplify():
    from sympy.physics.units.prefixes import kilo
    from sympy.physics.units import foot, inch
    
    result = quantity_simplify(kilo*foot*inch)
    assert result == 250*foot**2/3
    
    result = quantity_simplify(foot - 6*inch)
    assert result == foot/2


def test_check_dimensions():
    x = symbols('x')
    
    # Should not raise for dimensionally consistent expressions
    check_dimensions(meter + 2*meter)
    check_dimensions(meter*kilogram)
    
    # Should raise for dimensionally inconsistent expressions
    with raises(ValueError):
        check_dimensions(meter + second)
    
    with raises(ValueError):
        check_dimensions(meter + 1)
