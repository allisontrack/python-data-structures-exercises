def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    phrase_list = [letter.swapcase() if letter.upper() == to_swap.upper() else letter for letter in phrase]
    return ''.join(phrase_list)


print(flip_case('ApQsT', 'p'))
print(flip_case('Aaaahhh', 'A'))
print(flip_case('Aaaahhh', 'h'))