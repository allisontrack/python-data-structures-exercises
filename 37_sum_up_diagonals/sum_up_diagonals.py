def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """



    n = len(matrix)

    first_diagonal = [matrix[i][i] for i in range(n)]
    second_diagonal = [matrix[n-1-i][i] for i in range(n)]

    sum = 0

    for num in first_diagonal:
        sum = sum + num
    
    for num in second_diagonal:
        sum = sum + num

    print(sum)


m1 = [
    [1,   2],
    [30, 40],
]

sum_up_diagonals(m1)

m2 = [
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9],
]
sum_up_diagonals(m2)