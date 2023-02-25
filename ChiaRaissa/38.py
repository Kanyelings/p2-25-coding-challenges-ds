def ascii_to_string(array):
    string = " "
    for val in array:
        string = chr(val) + string
        return string
    print(ascii_to_string([95, 35, 54, 40]))
