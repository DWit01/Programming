def dry_streak(rainfall):
    """
    Return the longest run of consecutive dry days (0 mm) in the list rainfall as an integer. Return 0 if there are no dry days.
    """
    longest = 0
    current = 0
    for amount in rainfall:
        if amount == 0:
            current += 1
            if current > longest:
                longest = current
        else:
            current = 0
    return longest


def test_dry_streak():
    # Examples from Worked example (coursework-description.pdf)
    assert dry_streak([0, 0, 3, 0, 0, 0, 1, 0]) == 3
    # No dry days
    assert dry_streak([2, 5, 1]) == 0
    # Empty list
    assert dry_streak([]) == 0
    # Every day dry
    assert dry_streak([0, 0, 0]) == 3
    print("All dry_streak tests passed")


def main():
    # test code
    test_dry_streak()


if __name__ == "__main__":
    main()