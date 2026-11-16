def image_smooth(image):
    """
    Return a new image where each pixel is averaged with its up, down, left and right neighbours that exist, rounded down.
    """
    height = len(image) # Get the number of rows in the image
    width = len(image[0]) # Get the number of columns in the image
    new_image = []
    for r in range(height): # (r = row index) Loop through each row of the image
        new_row = [] 
        for c in range(width): # (c = column index) Loop through each column of the image
            values = [image[r][c]] # Start with the current pixel value
            if r > 0:
                values.append(image[r - 1][c])  # up (r - 1, c = row above, same column)
            if r < height - 1:
                values.append(image[r + 1][c])  # down (r + 1, c = row below, same column)
            if c > 0:
                values.append(image[r][c - 1])  # left (r, c - 1 = same row, column to the left)
            if c < width - 1:
                values.append(image[r][c + 1])  # right (r, c + 1 = same row, column to the right)
            new_row.append(int(sum(values) / len(values))) # Calculate the average of the pixel and its neighbours then round down and add to the new row
        new_image.append(new_row) # Add the new row to the new image
    return new_image


def test_image_smooth():
    # Examples from Worked example (coursework-description.pdf)
    assert image_smooth([[0, 0, 0], [0, 9, 0], [0, 0, 0]]) == [[0, 2, 0], [2, 1, 2], [0, 2, 0]]
    assert image_smooth([[1, 2], [3, 4]]) == [[2, 2], [2, 3]]

    # Print test passed message if all tests pass, if any test fails, an assertion error will be raised and the message will not be printed
    print("All image_smooth tests passed")


def main():
    # Test code
    test_image_smooth()


if __name__ == "__main__":
    main()