def coin_bias(tosses):
    """
    Return True if the drift (heads minus tails) is outside -√n to +√n, where n is the number of tosses.
    """
    drift = tosses.count("H") - tosses.count("T") # Calculate the drift by counting the number of heads and tails and subtracting them
    return drift ** 2 > len(tosses) # Square the drift and compare it to the number of tosses to check if it exceeds the square root limit

def test_coin_bias():
    # Examples from Worked example (coursework-description.pdf)
    assert coin_bias("HHHHTH") == True
    assert coin_bias("HTTHHT") == False
    assert coin_bias("HHHT") == False
    # Empty string gives False
    assert coin_bias("") == False

    # Print test passed message if all tests pass, if any test fails, an assertion error will be raised and the message will not be printed
    print("All coin_bias tests passed")


def main():
    # Test code
    test_coin_bias()


if __name__ == "__main__":
    main()