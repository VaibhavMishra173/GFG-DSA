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

def towerOfHanoi(n, a, b, c):
    """
    Solves the Tower of Hanoi problem for `n` disks.

    The Tower of Hanoi is a mathematical puzzle where you have three rods (A, B, and C) and `n` disks of different sizes 
    which can slide onto any rod. The puzzle starts with the disks neatly stacked in ascending order of size on one rod, 
    the smallest at the top, making a conical shape.

    The objective of the puzzle is to move the entire stack to another rod, following these rules:
    1. Only one disk can be moved at a time.
    2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack.
    3. No larger disk may be placed on top of a smaller disk.

    Parameters:
    - n (int): Number of disks.
    - a (str): The name of the source rod.
    - b (str): The name of the auxiliary rod.
    - c (str): The name of the target rod.

    This function prints the steps required to solve the Tower of Hanoi problem for `n` disks.
    
    Example:
        towerOfHanoi(2, 'A', 'B', 'C')
        # Output:
        # Move 1 from A to C
        # Move 2 from A to B
        # Move 1 from C to B

        towerOfHanoi(3, 'A', 'B', 'C')
        # Output:
        # Move 1 from A to C
        # Move 2 from A to B
        # Move 1 from C to B
        # Move 3 from A to C
        # Move 1 from B to A
        # Move 2 from B to C
        # Move 1 from A to C
    """
    if n == 1:
        print(f'Move 1 from {a} to {c}')
        return
    towerOfHanoi(n-1, a, c, b)
    print(f'Move {n} from {a} to {c}')
    towerOfHanoi(n-1, b, a, c)


towerOfHanoi(2, 'a', 'b', 'c')
print('------------------')
towerOfHanoi(3, 'a', 'b', 'c')

def josephusProblem(n, k):
    """
    Solves the Josephus problem using recursion.

    In the Josephus problem, there are `n` people standing in a circle. Starting from a particular position, 
    every `k`-th person is eliminated from the circle, and the process continues until only one person remains. 
    The function returns the position (0-based index) of the last remaining person.

    Parameters:
    n (int): The number of people in the circle.
    k (int): The step count at which people are eliminated (1-based).

    Returns:
    int: The position (0-based index) of the last remaining person.
    
    Examples:
    >>> josephusProblem(4, 2)
    0
    >>> josephusProblem(5, 3)
    3
    """
    if n == 1:
        return 0
    else:
        return (josephusProblem(n-1, k) + k) % n

# Test cases
n = 4
k = 2
print(josephusProblem(n, k))  # Output: 0

n = 5
k = 3
print(josephusProblem(n, k))  # Output: 3

def subsetSum(arr, n, s):
    """
    Determines the number of subsets of a given array that sum up to a specific target value.

    This function uses recursion to explore all possible subsets of the array and counts how many of them
    have a sum equal to the target value `s`.

    Parameters:
    arr (list of int): The list of integers from which subsets are formed.
    n (int): The number of elements to consider from the array.
    s (int): The target sum for the subsets.

    Returns:
    int: The number of subsets that sum up to the target value `s`.

    Base Cases:
    - If the sum `s` is 0, the function returns 1, as the empty subset always has a sum of 0.
    - If `n` is 0 and `s` is not 0, the function returns 0, since no subset can be formed without elements.

    Example:
    >>> arr = [10, 5, 2, 3, 6]
    >>> s = 8
    >>> subsetSum(arr, len(arr), s)
    2  # Subsets are [5, 3] and [2, 6]
    """
    # Base cases
    if s == 0:
        return 1  # A subset with sum 0 always exists (the empty subset)
    if n == 0:
        return 0  # If no elements are left and sum is not zero, no subset can be formed

    # If the current element is greater than the sum, ignore it
    if arr[n-1] > s:
        return subsetSum(arr, n-1, s)

    # Otherwise, consider the element in the subset or exclude it
    return subsetSum(arr, n-1, s) + subsetSum(arr, n-1, s - arr[n-1])


# Test case
arr = [10, 5, 2, 3, 6]
s = 8
print(subsetSum(arr, len(arr), s))  # Output: 2

def perOfStr(s):
    """
    Generates all permutations of the given string using recursion.

    Parameters:
    s (str): The input string.

    Returns:
    list of str: A list containing all permutations of the string.
    
    Example:
    >>> perOfStr('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    """
    # Base case: If the string has only one character, return it as the only permutation
    if len(s) == 1:
        return [s]

    # Recursive case: Generate permutations by fixing each character in the string
    perms = []
    for i in range(len(s)):
        # Remove the current character and get permutations of the remaining string
        remaining = s[:i] + s[i+1:]
        for p in perOfStr(remaining):
            perms.append(s[i] + p)

    return perms

# Test case
print(perOfStr('abc'))  # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
