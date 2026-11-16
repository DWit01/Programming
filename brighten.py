def brighten(image, amount):
    """
    Return a new image with amount added to every pixel, keeping each value between 0 and 255.
    """
    new_image = [] # Create a new empty list to hold the image
    for row in image: # Loop through each row in the image
        new_row = [] # Create a new empty list to hold the row
        for pixel in row:
            value = pixel + amount # Add the amount to the pixel value
            if value > 255:
                value = 255 # If the value is greater than 255, set it to 255
            elif value < 0:
                value = 0 
            new_row.append(value) # Append the new pixel value to the new row
        new_image.append(new_row) # Append the new row to the new image
    return new_image


def test_brighten():
    # Examples from Worked example (coursework-description.pdf)
    assert brighten([[250, 10], [128, 0]], 10) == [[255, 20], [138, 10]]
    # Negative amount darkens and values below 0 become 0
    assert brighten([[5, 100]], -10) == [[0, 90]]

    # Print test passed message if all tests pass, if any test fails, an assertion error will be raised and the message will not be printed
    print("All brighten tests passed")


def main():
    # Test code
    test_brighten()


if __name__ == "__main__":
    main()