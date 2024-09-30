def digitalRoot(n):
    """
    Computes the digital root of a number using recursion.
    
    The digital root is the recursive sum of all the digits in a number, until a single-digit number is obtained.

    Parameters:
    n (int): The input number.

    Returns:
    int: The digital root of the number.

    Example:
    >>> digitalRoot(99999)
    9
    """
    # Base case: if n is a single-digit number, return it
    if n < 10:
        return n

    # Recursive case: sum the digits of the number and call digitalRoot again
    res = digitalRoot(n // 10) + (n % 10)

    # Continue reducing the result to a single digit
    return digitalRoot(res)


# Test case
print(digitalRoot(99999))  # Output: 9
