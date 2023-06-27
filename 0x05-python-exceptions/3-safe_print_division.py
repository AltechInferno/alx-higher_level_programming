#!/usr/bin/python3
#3-safe-print-division 

def safe_print_division(x, y):
    """Returns division of x by y."""
    try:
        div = x / y
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)

