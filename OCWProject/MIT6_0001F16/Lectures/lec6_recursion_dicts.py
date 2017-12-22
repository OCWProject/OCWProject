# MIT6.0001- LECTURE 6: RECURSION, DICTIONARIES

# Recursion

# Factorial calculate by recursion method
def factR(n):
    """
    Factorial calculate by recursion method
    :param n: integer greater than 0
    :return: factorial of n
    """
    if n <= 1:
        return n
    else:
        return n * factR(n - 1)
print(factR(15))
