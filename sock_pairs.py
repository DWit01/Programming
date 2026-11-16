def sock_pairs(socks):
    """
    Return the number of matching pairs of socks in the list.
    """

    unmatched = [] # An empty list to keep track of unmatched socks
    matched = 0 #  A counter to keep track of the number of matched pairs

    for sock in socks:
        if sock in unmatched:
            unmatched.remove(sock) # Remove the sock from unmatched if it is found, this = a match
            matched += 1
        else:
            unmatched.append(sock) # Add the sock to unmatched if it is not found, this = no match
    return matched

def test_sock_pairs():
    # Examples from Worked example (coursework-description.pdf)
    assert sock_pairs(["red", "blue", "red", "green", "blue"]) == 2
    # No matching socks gives 0
    assert sock_pairs(["red", "blue", "green"]) == 0
    # Empty list gives 0
    assert sock_pairs([]) == 0

    # Print test passed message if all tests pass, if any test fails, an assertion error will be raised and the message will not be printed
    print("All sock_pairs tests passed")

def main():
    # Test code
    test_sock_pairs()

if __name__ == "__main__":
    main()
