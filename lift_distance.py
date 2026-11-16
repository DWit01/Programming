def lift_distance(floors):
    """
    Return the total number of floors the lift travelled between its stops, as an integer.
    """
    total = 0
    # i = index of the current stop, starting from 1
    for i in range(1, len(floors)): # Using range starting from 1 to avoid index error, using len(floors) to get the number of stops
        total += abs(floors[i] - floors[i - 1]) # Using abs() to ensure we always add a positive distance
    return total


def test_lift_distance():
    # Examples from Worked example (coursework-description.pdf)
    assert lift_distance([0, 5, 2, 2, 7]) == 13
    # Fewer than two stops gives 0
    assert lift_distance([]) == 0
    assert lift_distance([4]) == 0

    # Print test passed message if all tests pass, if any test fails, an assertion error will be raised and the message will not be printed
    print("All lift_distance tests passed")


def main():
    # Test code
    test_lift_distance()


if __name__ == "__main__":
    main()