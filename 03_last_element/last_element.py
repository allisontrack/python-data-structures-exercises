def last_element(list):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """

    if not list:
        return None
    else:
        return list[-1]


print(last_element([1, 2, 3]))