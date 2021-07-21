def sum_floats(nums):
    """Return sum of floating point numbers in nums.
    
        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9
        
        >>> sum_floats([1, 2, 3])
        0
    """

    # hint: to find out if something is a float, you should use the
    # "isinstance" function --- research how to use this to find out
    # if something is a float!


    def filter_floats(item):
        if isinstance(item, float):
            return True
        else:
            return False

    filtered_nums = filter(filter_floats, nums)

    value = 0

    for num in filtered_nums:
        value = value + num

    return value

print(sum_floats([1.5, 2.4, 'awesome', [], 1]))
print(sum_floats([1, 2, 3]))