from sympy.combinatorics.permutations import Permutation

def test_issue_reproduction():
    # This should construct the identity permutation by applying cycles left-to-right
    # [0,1] followed by [0,1] should result in identity
    # Currently raises ValueError but should return identity permutation
    perm = Permutation([[0,1],[0,1]])
    
    # The result should be the identity permutation
    # Identity permutation maps each element to itself
    assert perm(0) == 0
    assert perm(1) == 1
    
    # Should also equal the explicit identity permutation
    identity = Permutation([])
    assert perm == identity