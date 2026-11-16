def firing_pattern(motif, seconds):
    """
    Return how many spikes "1"s the repeating motif fires in the first seconds seconds.
    """
    spikes = 0
    for second in range(seconds):
        if motif[second % len(motif)] == "1": # Check if character in motif at the current second is "1"
            spikes += 1 # Increment spikes if the character is 1
    return spikes


def test_firing_pattern():
    # Examples from Worked example (coursework-description.pdf)
    assert firing_pattern("110", 7) == 5
    # Seconds of 0 gives 0
    assert firing_pattern("110", 0) == 0

    # Print test passed message if all tests pass, if any test fails, an assertion error will be raised and the message will not be printed
    print("All firing_pattern tests passed")


def main():
    # Test code
    test_firing_pattern()


if __name__ == "__main__":
    main()