def is_binary_mutation_list(codes):
    """
    Return True if every neighbouring pair of codes differs in exactly one position, otherwise False.
    """
    for i in range(1, len(codes)): # Loop through the codes starting from the second code (index 1)
        differences = 0
        for position in range(len(codes[i])): # Loop through each position in the current code
            if codes[i][position] != codes[i - 1][position]: # Check if the current position in the current code is different from the same position in the previous code
                differences += 1 # Count the number of differences between the current code and the previous code
        if differences != 1: # If the number of differences is not equal to 1, return False
            return False
    return True


def test_is_binary_mutation_list():
    # Examples from Worked example (coursework-description.pdf)
    assert is_binary_mutation_list(["001", "000", "100"]) == True
    assert is_binary_mutation_list(["0000", "1000", "1111"]) == False
    # Zero or one code gives True
    assert is_binary_mutation_list([]) == True
    assert is_binary_mutation_list(["101"]) == True

    # Print test passed message if all tests pass, if any test fails, an assertion error will be raised and the message will not be printed
    print("All is_binary_mutation_list tests passed")


def main():
    # Test code
    test_is_binary_mutation_list()


if __name__ == "__main__":
    main()