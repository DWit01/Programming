def initials(*names):
    """
    Return the capitalised first letter of each name, in order, each followed by a full stop, joined into one string.
    """
    result = ""
    for name in names:
        result += name[0].upper() + "." # Add the first letter of the name capitalised followed by a "."
    return result


def test_initials():
    # Examples from Worked example (coursework-description.pdf)
    assert initials("ada", "lovelace") == "A.L."
    assert initials("john", "ronald", "reuel", "tolkien") == "J.R.R.T."
    # At least one name is always given
    assert initials("daniel") == "D."

    # Print test passed message if all tests pass, if any test fails, an assertion error will be raised and the message will not be printed
    print("All initials tests passed")


def main():
    # Test code
    test_initials()


if __name__ == "__main__":
    main()