import pytest
from sympy.physics import units
from sympy.physics.units.systems.si import SI
from sympy import symbols

def test_issue_reproduction():
    # Create symbols with different but equivalent dimensions
    # velocity has dimension [length]/[time]
    # acceleration*time has dimension [length]/[time]^2 * [time] = [length]/[time]
    v1 = symbols('v1')
    a1 = symbols('a1')
    t1 = symbols('t1')
    
    # Set up the dimensions - velocity and acceleration*time should be equivalent
    velocity_expr = v1 * units.meter / units.second
    accel_time_expr = a1 * units.meter / units.second**2 * t1 * units.second
    
    # This should work since both expressions have the same dimension [length]/[time]
    # But currently fails because the dimension comparison doesn't recognize equivalence
    combined_expr = velocity_expr + accel_time_expr
    
    # This should not raise an error, but currently does
    factor, dimension = SI._collect_factor_and_dimension(combined_expr)