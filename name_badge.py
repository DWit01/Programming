def name_badge(name, role):
    """
    Return a badge string in the form "Hi, I'm <name> (<role>)".
    """
    return (f"Hi, I'm {name} ({role})")


def test_name_badge():
    # Examples from Worked example (coursework-description.pdf)
    assert name_badge("Sam", "Teacher") == "Hi, I'm Sam (Teacher)"
    # Another name and role
    assert name_badge("Daniel", "Student") == "Hi, I'm Daniel (Student)"

    # Print test passed message if all tests pass, if any test fails, an assertion error will be raised and the message will not be printed
    print("All name_badge tests passed")
    

def main():
    # Test code
    test_name_badge()


if __name__ == "__main__":
    main()