from data_utils import load_data


def rainfall_summary(rows):
    """
    Return months used, mean rainfall to 1 dp, year of wettest month, month of wettest month.
    """
    months_used = 0
    total = 0
    wettest_rain = -1
    wettest_year = 0
    wettest_month = 0
    for row in rows:
        if len(row) != 7: # Skip rows that don't have 7 columns
            continue
        rain_text = row[5] # Get the rainfall value from the 6th column (index 5)
        if rain_text == "---": # Skip rows where rainfall data is missing
            continue 
        if rain_text.endswith("*"): # Remove the asterisk if present
            rain_text = rain_text[:-1]
        rain = float(rain_text) # Convert the rainfall value to a float
        months_used += 1 # Count the number of months with valid rainfall data
        total += rain
        if rain > wettest_rain:
            wettest_rain = rain
            wettest_year = int(row[0]) # Get the year from the first column (index 0)
            wettest_month = int(row[1]) # Get the month from the second column (index 1)
    mean = round(total / months_used, 1) # Calculate the mean rainfall round to 1 decimal place
    return [months_used, mean, wettest_year, wettest_month]


def test_rainfall_summary(rows):
    # Examples from Worked example (coursework-description.pdf)
    example_rows = [
        ["1959", "1", "4.0", "-2.0", "25", "40.9", "54.1"],
        ["1959", "2", "6.6", "2.1", "10", "---", "17.8"],
        ["1959", "3", "10.6", "4.2", "0", "81.3*", "85.7"],
        ["Site", "closed"],
    ]
    assert rainfall_summary(example_rows) == [2, 61.1, 1959, 3]
    # Two equally wet months keeps the first one
    tie_rows = [
        ["2000", "1", "5.0", "1.0", "3", "50.0", "40.0"],
        ["2000", "2", "5.0", "1.0", "3", "50.0", "40.0"],
    ]
    assert rainfall_summary(tie_rows) == [2, 50.0, 2000, 1]
    # Result from the real data file
    assert rainfall_summary(rows) == [621, 98.8, 2006, 12]
    print("All rainfall_summary tests passed")


def main():
    # Load the Paisley weather data. rows is a list, and each item in it is
    # one line of the file as a list of strings.
    rows = load_data("paisleydata.txt")

    # Print the head and tail of the data
    for row in rows[:5]:
        print(row)
    print(".\n.\n.")
    for row in rows[-5:]:
        print(row)

    # Test code
    print(rainfall_summary(rows))
    test_rainfall_summary(rows)


if __name__ == "__main__":
    main()