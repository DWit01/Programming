def space_shuttle(n, engine_present=True):
    """
    Return a countdown string from n, each number followed by three dots "...", ending with the message for the engine state.
    """
    if n < 0:
        return "Ground Control, we have a problem"
    countdown = ""
    if engine_present:
        for number in range(n, 0, -1): # Using range starting from n down to 1, decrementing by 1 each time
            countdown += str(number) + "..." # Using str(number) to convert the number to a string and add it with "..." to the countdown string
        return countdown + "Liftoff!"
    for number in range(n, -1, -1): # Using range starting from n down to -1, decrementing by 1 each time
        countdown += str(number) + "..."
    return countdown + "That's another fine mess you've gotten me into, Stan"


def test_space_shuttle():
    # Examples from Worked example (coursework-description.pdf)
    assert space_shuttle(3) == "3...2...1...Liftoff!"
    assert space_shuttle(3, False) == "3...2...1...0...That's another fine mess you've gotten me into, Stan"
    assert space_shuttle(0) == "Liftoff!"
    assert space_shuttle(-1) == "Ground Control, we have a problem"
    # Below 0 gives the same message no matter the engine is present
    assert space_shuttle(-1, False) == "Ground Control, we have a problem"

    # Print test passed message if all tests pass, if any test fails, an assertion error will be raised and the message will not be printed
    print("All space_shuttle tests passed")


def main():
    # Test code
    test_space_shuttle()


if __name__ == "__main__":
    main()