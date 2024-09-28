def printBinary(n):
    """
    Recursively prints the binary representation of a given integer n.
    
    The function works by dividing the number by 2 (integer division)
    and printing the remainder (which will be either 0 or 1) after the
    recursive call. This simulates how binary numbers are built from
    their least significant bit upwards.
    
    Args:
        n (int): The integer to convert to binary.
        
    Returns:
        None: The function prints the binary digits without returning anything.
        
    Example:
        >>> printBinary(16)
        10000
    """
    if n == 0:
        return
    printBinary(n // 2)
    print(n % 2)

print(printBinary(16))

def printNTo1(n):
    """
    Recursively prints numbers from n down to 1.

    The function works by printing the current value of n, then calling 
    itself with the value of n-1, continuing until n reaches 0.

    Args:
        n (int): The starting integer to print from.
        
    Returns:
        None: The function prints the numbers without returning anything.
        
    Example:
        >>> printNTo1(5)
        5
        4
        3
        2
        1
    """
    if n == 0:
        return
    print(n)
    printNTo1(n - 1)

printNTo1(16)

def print1ToN(n):
    """
    Recursively prints numbers from 1 up to n.

    The function works by first calling itself with n-1, and then printing the
    current value of n, ensuring that numbers are printed in ascending order.

    Args:
        n (int): The ending integer to print up to.
        
    Returns:
        None: The function prints the numbers without returning anything.
        
    Example:
        >>> print1ToN(5)
        1
        2
        3
        4
        5
    """
    if n == 0:
        return
    print1ToN(n - 1)
    print(n)

print1ToN(16)

def factorial(n):
    """
    Recursively calculates the factorial of a given number n.

    The factorial of a number n is the product of all positive integers less 
    than or equal to n. The function uses recursion, where the factorial of n 
    is calculated as n * factorial(n-1), with the base case being that the 
    factorial of 0 or 1 is 1.

    Args:
        n (int): The integer for which the factorial is to be calculated.
        
    Returns:
        int: The factorial of the input number n.
        
    Example:
        >>> factorial(5)
        120
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

def fibonacci(n):
    """
    Recursively calculates the nth Fibonacci number.

    The Fibonacci sequence is defined as:
    - Fibonacci(0) = 0
    - Fibonacci(1) = 1
    - Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2) for n > 1

    The function uses recursion to compute the nth Fibonacci number by 
    summing the two preceding numbers in the sequence.

    Args:
        n (int): The position in the Fibonacci sequence to compute.
        
    Returns:
        int: The nth Fibonacci number.
        
    Example:
        >>> fibonacci(5)
        5
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))
