def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    num_count_1 = {}
    num_count_2 = {}

    for num in str(num1):
        if num in num_count_1:
            num_count_1[num] += 1
        else:
            num_count_1[num] = 1
        
    for num in str(num2):
        if num in num_count_2:
            num_count_2[num] += 1
        else:
            num_count_2[num] = 1

    if num_count_1 == num_count_2:
        return True
    else:
        return False

print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
print(same_frequency(1212, 2211))