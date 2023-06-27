#!/usr/bin/python3
# 0-safe_print_list.py


def safe_print_list(my_list=[], y=0):
    """Print y elememts of a list.

    Args:
        my_list (list): The list to print elements from.
        y (int): The number of elements of my_list to print.

    Returns:
         number of elements printed.
    """
    j = 0
    for index in range(y):
        try:
            print("{}".format(my_list[index]), end="")
            j += 1
        except IndexError:
            break
    print("")
    return (j)
