import pytest
from sympy.parsing.mathematica import parse_mathematica

def test_issue_reproduction():
    # This should work but currently fails due to Greek character not being recognized as valid identifier
    result = parse_mathematica('λ')
    # The test expects this to return a Symbol named 'λ' (lambda)
    assert str(result) == 'λ'