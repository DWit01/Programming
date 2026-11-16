def redact(sentence, banned):
    """
    Return sentence with every word that exactly matches one in banned replaced by the same number of asterisks.
    """
    words = [] # Create an empty list to hold the words of the new sentence
    for word in sentence.split(): # Split the sentence into words
        if word in banned:
            words.append("*" * len(word)) # Replace the banned word with asterisks of the same length
        else:
            words.append(word) # Keep the word unchanged if it's not banned
    return " ".join(words) 


def test_redact():
    # Examples from Worked example (coursework-description.pdf)
    assert redact("the cat sat on the mat", ["cat", "mat"]) == "the *** sat on the ***"
    # Nothing banned gives the sentence unchanged
    assert redact("Daniel codes", []) == "Daniel codes"

    # Print test passed message if all tests pass, if any test fails, an assertion error will be raised and the message will not be printed
    print("All redact tests passed")


def main():
    # Test code
    test_redact()


if __name__ == "__main__":
    main()