# Convert radians into degrees!

import math  # For the pi function

# Ask for input from the user. Convert that input into degrees.
def convert_radians():
    is_number = False

    while is_number != True:
        try:
            radian = float(input("Input radian value to convert: "))
            degree = float((radian * (180 / math.pi)))

            print(degree)
            return True
        except:
            print("Please input a number value.")


convert_radians()
