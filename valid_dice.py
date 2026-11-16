def valid_dice(roll):
    """
    Return True if roll could come up on an ordinary six-sided dice, otherwise False.
    """
    return roll in [1, 2, 3, 4, 5, 6] # Using a list to check if the roll is in the range(1-6)


def test_valid_dice():
    # Examples from Worked example (coursework-description.pdf)
    assert valid_dice(4) == True
    assert valid_dice(7) == False
    # Boundaries 1 and 6 are on the dice and 0 is not
    assert valid_dice(1) == True
    assert valid_dice(6) == True
    assert valid_dice(0) == False

    # Print test passed message if all tests pass, if any test fails, an assertion error will be raised and the message will not be printed
    print("All valid_dice tests passed")


def main():
    test_valid_dice()


if __name__ == "__main__":
    main()