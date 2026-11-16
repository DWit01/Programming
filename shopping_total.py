def shopping_total(prices):
    """
    Return the total of prices, adding 3.5 delivery if the total is under 20.
    """
    if len(prices) == 0: # Len(prices) == 0 is used to check if the list is empty, if it is, return 0
        return 0
    total = sum(prices) # Sum(prices) is used to calculate the total of the prices in the list
    if total < 20:
        total += 3.5
    return total


def test_shopping_total():
    # Examples from Worked example (coursework-description.pdf)
    assert shopping_total([5, 8.5, 4]) == 21.0
    assert shopping_total([12, 8]) == 20
    assert shopping_total([]) == 0
    # Just under 20 gets delivery
    assert shopping_total([19]) == 22.5

    # Print test passed message if all tests pass, if any test fails, an assertion error will be raised and the message will not be printed
    print("All shopping_total tests passed")


def main():
    # Test code
    test_shopping_total()


if __name__ == "__main__":
    main()