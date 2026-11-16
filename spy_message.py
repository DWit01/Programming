def spy_message(note, secret):
    """
    Return True if the letters of secret can be found in order using each note character only once.
    """
    position = 0 # Keep track of the current position in the secret string
    for character in note:
        if position < len(secret) and character == secret[position]: # Check if the current character in note matches the current character in secret
            position += 1 # Increment to check the next character in secret
    return position == len(secret)


def test_spy_message():
    # Examples from Worked example (coursework-description.pdf)
    assert spy_message("meet at the park", "mat") == True
    assert spy_message("meet at the park", "tam") == False
    assert spy_message("Daniel can code", "Dcc") == True
    assert spy_message("ab", "aa") == False

    # Print test passed message if all tests pass, if any test fails, an assertion error will be raised and the message will not be printed
    print("All spy_message tests passed")


def main():
    # Test code
    test_spy_message()


if __name__ == "__main__":
    main()