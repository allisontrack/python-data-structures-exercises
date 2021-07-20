def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

    phrase_backwards = phrase[::-1]
    return phrase_backwards


reverse_string('awesome')
reverse_string('sauce')