from sympy import symbols, expand
from sympy.physics.quantum import TensorProduct

def test_issue_reproduction():
    # Create symbols
    a, b, c = symbols('a b c')
    A, B = symbols('A B', commutative=False)
    
    # Create a TensorProduct with scalar factors in summands
    # This should expand to: a*A*B + b*A*B + c*A*B = (a + b + c)*A*B
    tp = TensorProduct(a + b + c, A*B)
    
    # Expand the tensor product
    expanded = tp.expand(tensorproduct=True)
    
    # The expected result should be fully expanded
    expected = a*TensorProduct(A, B) + b*TensorProduct(A, B) + c*TensorProduct(A, B)
    
    # This assertion will fail because the current implementation doesn't
    # properly handle recursive expansion when scalar factors are present
    assert expanded == expected, f"Expected {expected}, got {expanded}"