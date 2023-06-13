#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Check if the input list is None
    if my_list is None:
        return

    # Check if the index is out of bounds
    if idx < 0 or idx >= len(my_list):
        return my_list[:]

     # Construct a new list with the element replaced
    return my_list[:idx] + [element] + my_list[idx+1:]

