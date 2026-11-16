def can_ride(height):
    """
    Returns True if the height meets the 120 cm minimum, otherwise returns False.
    """
    return height >= 120


def main():
    # Examples from Worked example (coursework-description.pdf)
    assert can_ride(135) == True
    assert can_ride(119) == False

    # Boundary - exactly the minimum is allowed
    assert can_ride(120) == True

    # Just either side of the boundary
    assert can_ride(120.1) == True
    assert can_ride(119.9) == False

    # Zero height
    assert can_ride(0) == False

    # Print test passed message if all tests pass, if any test fails, an assertion error will be raised and the message will not be printed
    print("All can_ride tests passed")


if __name__ == "__main__":
    main()