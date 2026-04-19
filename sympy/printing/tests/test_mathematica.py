from sympy import symbols, sin, cos, pi, oo, Integral, Sum, Derivative, Float
from sympy.printing.mathematica import mathematica_code
from sympy.utilities.pytest import raises


def test_Integer():
    assert mathematica_code(5) == "5"
    assert mathematica_code(-5) == "-5"


def test_Rational():
    assert mathematica_code(1, 2) == "1/2"
    assert mathematica_code(-1, 2) == "-1/2"


def test_Function():
    f = symbols('f', cls=Function)
    assert mathematica_code(f(x)) == "f[x]"
    assert mathematica_code(sin(x)) == "Sin[x]"
    assert mathematica_code(cos(x)) == "Cos[x]"


def test_Pow():
    x, y = symbols('x y')
    assert mathematica_code(x**y) == "x^y"
    assert mathematica_code(x**(y**z)) == "x^(y^z)"
    assert mathematica_code((x**y)**z) == "(x^y)^z"


def test_Mul():
    x, y, z = symbols('x y z')
    assert mathematica_code(x*y*z) == "x*y*z"
    assert mathematica_code(x*y**z) == "x*y^z"
    assert mathematica_code((x*y)**z) == "(x*y)^z"


def test_constants():
    assert mathematica_code(pi) == "Pi"
    assert mathematica_code(oo) == "Infinity"
    assert mathematica_code(-oo) == "-Infinity"


def test_containers():
    assert mathematica_code([1, 2, 3, [4, 5, [6, 7]], 8, [9, 10]]) == \
        "{1, 2, 3, {4, 5, {6, 7}}, 8, {9, 10}}"
    assert mathematica_code((1, 2, (3, 4))) == "{1, 2, {3, 4}}"
    assert mathematica_code([1]) == "{1}"
    assert mathematica_code((1,)) == "{1}"


def test_Integral():
    x, y = symbols('x y')
    assert mathematica_code(Integral(sin(x), x)) == "Hold[Integrate[Sin[x], x]]"
    assert mathematica_code(Integral(x*y, (x, 0, 1), (y, -1, 1))) == \
        "Hold[Integrate[x*y, (x, 0, 1), (y, -1, 1)]]"


def test_Sum():
    x, y, z = symbols('x y z')
    assert mathematica_code(Sum(sin(x), (x, 0, 10))) == \
        "Hold[Sum[Sin[x], (x, 0, 10)]]"
    assert mathematica_code(Sum(exp(x), (x, 0, oo))) == \
        "Hold[Sum[Exp[x], (x, 0, Infinity)]]"


def test_Derivative():
    x, y, z, t = symbols('x y z t')
    f = symbols('f', cls=Function)
    assert mathematica_code(Derivative(f(t), t)) == "D[f[t], t]"
    assert mathematica_code(Derivative(f(x, y), x)) == "D[f[x, y], x]"
    assert mathematica_code(Derivative(f(x, y), x, y)) == "D[f[x, y], x, y]"
    assert mathematica_code(Derivative(sin(x), x)) == "D[Sin[x], x]"


def test_Float():
    assert mathematica_code(Float('1.0e-4')) == "1.0*^-4"
    assert mathematica_code(Float('1.5e10')) == "1.5*^10"
    assert mathematica_code(Float('2.3e-15')) == "2.3*^-15"
    assert mathematica_code(Float('1.0')) == "1.0"
    assert mathematica_code(Float('-3.14e5')) == "-3.14*^5"


# Import symbols and Function for the tests
x, y, z = symbols('x y z')
from sympy import Function, exp
