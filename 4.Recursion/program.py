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

def sumOfN(n):
    """
    Recursively calculates the sum of all integers from 1 to n.

    The function works by recursively adding the current value of n to the sum 
    of integers from 1 to n-1. The base case is when n equals 1, in which case 
    the function returns 1.

    Args:
        n (int): The integer up to which the sum is calculated.
        
    Returns:
        int: The sum of all integers from 1 to n.
        
    Example:
        >>> sumOfN(5)
        15
    """
    if n == 1:
        return 1
    return n + sumOfN(n - 1)

print(sumOfN(5))

def isPalindrome(s, start, end):
    """
    Recursively checks whether a given string s is a palindrome.

    A palindrome is a word, phrase, or sequence that reads the same 
    backward as forward. The function compares the characters at the 
    start and end of the string and continues inward until all characters 
    are checked. If all character pairs are equal, the string is a palindrome.

    Args:
        s (str): The string to check for palindrome.
        start (int): The starting index for comparison.
        end (int): The ending index for comparison.
        
    Returns:
        bool: True if the string is a palindrome, otherwise False.
        
    Example:
        >>> isPalindrome('abbcbba', 0, len('abbcbba')-1)
        True
        >>> isPalindrome('geeks', 0, len('geeks')-1)
        False
    """
    if start >= end:
        return True
    return (s[start] == s[end] and isPalindrome(s, start + 1, end - 1))

s = 'abbcbba'
s1 = 'geeks'
print(isPalindrome(s, 0, len(s) - 1))   # Output: True
print(isPalindrome(s1, 0, len(s1) - 1)) # Output: False

def sumOfDigits(n):
    """
    Recursively calculates the sum of digits of a given number.

    This function takes a non-negative integer `n` and returns the sum of its digits. 
    It recursively divides the number by 10 and adds the remainder to the result 
    of the recursive call with the quotient.

    Parameters:
    n (int): A non-negative integer whose digits are to be summed.

    Returns:
    int: The sum of the digits of the number `n`.

    Example:
    >>> sumOfDigits(123)
    6
    """
    if n < 10:
        return n

    return n % 10 + sumOfDigits(n // 10)


print(sumOfDigits(123))

def maxPiece(n, a, b, c):
    """
    Recursively finds the maximum number of pieces that a given length `n` can be divided into,
    using pieces of lengths `a`, `b`, and `c`.

    This function attempts to cut the length `n` into the maximum possible number of pieces, 
    where each piece can have a length of `a`, `b`, or `c`. If it's not possible to cut 
    exactly into such pieces, it returns -1.

    Parameters:
    n (int): The total length to be divided.
    a (int): The length of the first type of piece.
    b (int): The length of the second type of piece.
    c (int): The length of the third type of piece.

    Returns:
    int: The maximum number of pieces `n` can be divided into, or -1 if it's not possible.

    Example:
    >>> maxPiece(23, 9, 11, 12)
    2

    >>> maxPiece(9, 2, 2, 2)
    4
    """
    if n == 0:
        return 0
    if n < 0:
        return -1

    res = max(maxPiece(n - a, a, b, c), maxPiece(n - b, a, b, c), maxPiece(n - c, a, b, c))

    if res == -1:
        return -1
    return res + 1


print(maxPiece(23, 9, 11, 12))  # Output: 2
print(maxPiece(9, 2, 2, 2))    # Output: 4

def generateSubsets(s, curr, i):
    """
    Recursively generates all subsets of a given string.

    This function generates all possible subsets (combinations of characters) 
    of the string `s` by recursively adding or skipping characters.

    Parameters:
    s (str): The original string from which subsets are generated.
    curr (str): The current subset being formed.
    i (int): The index of the current character being considered in the string.

    Example:
    >>> generateSubsets("abc", '', 0)
    '', 'c', 'b', 'bc', 'a', 'ac', 'ab', 'abc'
    """
    if i == len(s):
        print(curr)
        return
    # Exclude the current character and move to the next
    generateSubsets(s, curr, i + 1)
    # Include the current character and move to the next
    generateSubsets(s, curr + s[i], i + 1)

# Example usage:
s = "abc"
generateSubsets(s, '', 0)
