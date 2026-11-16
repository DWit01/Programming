def tide_turns(heights):
    """
    Return how many times the readings change direction between rising and falling.
    """
    turns = 0 # A counter to keep track of the number of turns
    for i in range(1, len(heights) - 1): # Loop through readings, excluding the first and last readings
        rising_before = heights[i] > heights[i - 1] # Check if current reading is rising compared to the previous reading
        rising_after = heights[i + 1] > heights[i] # Check if current reading is rising compared to the next reading
        if rising_before != rising_after:
            turns += 1 # Increment the turns counter
    return turns


def test_tide_turns():
    # Examples from Worked example (coursework-description.pdf)
    assert tide_turns([1, 3, 5, 4, 2, 3]) == 2
    # Fewer than three readings gives 0
    assert tide_turns([]) == 0
    assert tide_turns([1, 2]) == 0

    # Print test passed message if all tests pass, if any test fails, an assertion error will be raised and the message will not be printed
    print("All tide_turns tests passed")


def main():
    # Test code
    test_tide_turns()


if __name__ == "__main__":
    main()