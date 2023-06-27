#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Executes a function safely.

    Args:
        fct: function to execute.
        args: Arguments for fct.

    Returns:
        If an error occurs - None.
        Else - result of the call to fct.
    """
    try:
        result_final = fct(*args)
        return (result_final)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
