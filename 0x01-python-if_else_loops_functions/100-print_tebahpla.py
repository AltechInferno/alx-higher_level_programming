#!/usr/bin/python3
# A range for Lowercase alphabet in reverse
for i in range(122, 96, -1):
    # use this condition search every number and display it
    if i % 2 == 0:
        print("{:c}".format(i), end="")
    else:
        # display the left letters in uppercase
        print("{:c}".format(i - 32), end="")
