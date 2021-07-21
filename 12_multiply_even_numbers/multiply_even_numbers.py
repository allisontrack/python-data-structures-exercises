def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """


    def filter_nums(num) :
        if num % 2 == 0:
            return True
        else:
            return False
    
    filtered_nums = filter(filter_nums, nums)
    
    value = 1

    for num in filtered_nums:
        value = value * num
    
    return value

print(multiply_even_numbers([2, 3, 4, 5, 6]))
print(multiply_even_numbers([3, 4, 5]))
print(multiply_even_numbers([1, 3, 5]))