def clear_full_rows(grid):
    """
    Return a grid of the same size with every full row removed and same number of all 0 rows added at the top.
    """
    kept_rows = []
    for row in grid:
        if 0 in row:
            kept_rows.append(row) # Keep the row if it contains at least one 0
    new_grid = []
    for row in range(len(grid) - len(kept_rows)): # Add empty rows at the top of the grid to have the same size
        new_grid.append([0] * len(grid[0])) # Create a new row of 0s with same length as the original rows
    return new_grid + kept_rows # Return new grid with empty rows at the top and the kept rows


def test_clear_full_rows():
    # Examples from Worked example (coursework-description.pdf)
    assert clear_full_rows([[0, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [[0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 1]]
    # A single full row is a single empty row
    assert clear_full_rows([[1, 1, 1]]) == [[0, 0, 0]]
    
    # Print test passed message if all tests pass, if any test fails, an assertion error will be raised and the message will not be printed
    print("All clear_full_rows tests passed")


def main():
    # Test code
    test_clear_full_rows()


if __name__ == "__main__":
    main()