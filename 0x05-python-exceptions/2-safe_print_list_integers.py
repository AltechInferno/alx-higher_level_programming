#!/usr/bin/python3

def safe_print_list_integers(my_list=[], y=0):
    """Print first y elements of a list that are integers.

    Args:
        my_list (list): The list to print elements from.
        y (int): The number of elements of my_list to print.

    Returns:
        number of elements printed.
    """
    j = 0
    for index in range(0, y):
        try:
            print("{:d}".format(my_list[index]), end="")
            j += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (j)
