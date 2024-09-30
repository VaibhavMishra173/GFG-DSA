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

def isLucky(N, step=2):
    """
    Determines if a number N is a lucky number.

    A lucky number is one that is not removed through the recursive deletion process
    as described in the problem.

    Parameters:
    N (int): The number to check.
    step (int): The current step of the deletion process (default is 2).

    Returns:
    bool: True if the number is lucky, False otherwise.
    """
    # Base case: if the current step exceeds N, then N survived all deletions
    if step > N:
        return True
    
    # If N is divisible by the current step, it means N gets deleted
    if N % step == 0:
        return False
    
    # Recursively check for the next step with updated position of N
    # N's new position in the next iteration is N - N//step (the remaining numbers after deletion)
    new_N = N - (N // step)
    return isLucky(new_N, step + 1)

# Test cases
print(isLucky(5))   # Output: False (0)
print(isLucky(19))  # Output: True (1)
