from sympy import symbols
from sympy.solvers.polysys import solve_poly_system
import pytest

def test_issue_reproduction():
    x, y = symbols('x y')
    # This should raise NotImplementedError because the system has infinite solutions
    # (x = 1, y can be any value)
    with pytest.raises(NotImplementedError, match="only zero-dimensional systems supported"):
        solve_poly_system((x - 1,), x, y)