import sympy as sm

def test_issue_reproduction():
    # Create a 6x3 matrix with columns of twos in the first 3 rows
    # and a 3x3 identity matrix in the bottom 3 rows
    original = sm.Matrix([
        [2, 2, 2],
        [2, 2, 2], 
        [2, 2, 2],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])
    
    # Create a 6x1 column to insert
    insert_col = sm.Matrix([1, 1, 1, 1, 1, 1])
    
    # Insert the column at position 1
    result = original.col_insert(1, insert_col)
    
    # The expected result should maintain the row structure:
    # - First 3 rows should have twos with the inserted 1
    # - Last 3 rows should have the identity matrix with the inserted 1
    expected = sm.Matrix([
        [2, 1, 2, 2],
        [2, 1, 2, 2],
        [2, 1, 2, 2], 
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 0, 1]
    ])
    
    # This assertion should pass if col_insert works correctly
    # but will fail if the identity matrix rows are shifted to the top
    assert result == expected, f"Expected:\n{expected}\nGot:\n{result}"