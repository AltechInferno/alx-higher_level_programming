#!/usr/bin/python3
a = 89
b = 10
# Your code starts here
a = a ^ b
b = a ^ b
a = a ^ b
# Your code ends here
print("a={:d} - b={:d}".format(a, b))

