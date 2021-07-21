def list_check(list):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """

    for item in list:
        if not isinstance(item, list):
            return False
        else:
            return True


print(list_check([[1], [2, 3]]))
print(list_check([[1], "nope"]))