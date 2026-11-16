def film_length(minutes, units="hours"):
    """
    Return the film length as hours and minutes ("2h 15m") or as total seconds ("8100s").
    """
    if units == "seconds":
        return (f"{minutes * 60}s") # Convert minutes to seconds and return as a string
    hours = minutes // 60
    left = minutes % 60 # Calculate the leftover minutes after converting to hours
    return (f"{hours}h {left}m")


def test_film_length():
    # Examples from Worked example (coursework-description.pdf)
    assert film_length(135) == "2h 15m"
    assert film_length(60) == "1h 0m"
    assert film_length(45) == "0h 45m"
    assert film_length(135, "seconds") == "8100s"
    
    # Print test passed message if all tests pass, if any test fails, an assertion error will be raised and the message will not be printed
    print("All film_length tests passed")


def main():
    # Test code
    test_film_length()


if __name__ == "__main__":
    main()