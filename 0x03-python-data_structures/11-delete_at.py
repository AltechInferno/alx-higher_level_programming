#!/usr/bin/python3
def delete_at(list=[], idx=0):
    if idx < 0 or idx >= len(list):
        return (list)

    if list is None:
        return (None)

    del list[idx]
    return (list)
