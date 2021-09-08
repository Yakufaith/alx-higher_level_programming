#!/usr/bin/python3

import random

number = random.randint(-10, 10)

# Convert random generated number into string
text = str(number)

# Store last digit
last_digit = int(text[len(text) - 1])

# Print last digit
print("Last digit of {} is {} ".format(number, last_digit), end = "")

# Do some checks on the last digit
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
elif last_digit < 6 and last_digit != 0:
    print("and is less than 6 and not 0")
