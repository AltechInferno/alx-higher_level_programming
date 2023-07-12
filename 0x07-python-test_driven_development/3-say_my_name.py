""" name-printing function. """


def say_my_name(first_name, last_name=""):
    """Display a name.
    Args:
        first_name (str): first name to display.
        last_name (str):  last name to display.
    Raises:
        TypeError: If either of the firstname or lastname are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
