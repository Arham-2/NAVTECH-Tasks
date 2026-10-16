number = 10
if (number == 10):
    # First if statement
    if (number < 15):
        print("i is smaller than 15")
    # Nested - if statement
    # Will only be executed if statement above
    # it is true
    if (number < 12):
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")
