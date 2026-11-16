def sticky_key(text, key):
    """
    Return a new string from text with each character that matches key added twice.
    """
    result = ""
    for character in text:
        if character == key:
            result += character * 2 # Add the character twice if it matches the key
        else:
            result += character # Add the character once if it does not match the key
    return result


def test_sticky_key():
    # Examples from Worked example (coursework-description.pdf)
    assert sticky_key("hello", "l") == "hellllo"
    # No matching characters gives the text unchanged
    assert sticky_key("daniel", "s") == "daniel"
    # Empty text gives an empty string
    assert sticky_key("", "a") == ""

    # Print test passed message if all tests pass, if any test fails, an assertion error will be raised and the message will not be printed
    print("All sticky_key tests passed")


def main():
    # Test code
    test_sticky_key()


if __name__ == "__main__":
    main()