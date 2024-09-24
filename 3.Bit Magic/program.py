def leftShift(n, times):
    """
    Performs a left bitwise shift operation.
    
    Args:
        n (int): The number to be shifted.
        times (int): The number of positions to shift left.
    
    Returns:
        int: The result of shifting 'n' to the left by 'times' positions.
    """
    return n << times

print(leftShift(3, 1))  # Output: 6


def rightShift(n, times):
    """
    Performs a right bitwise shift operation.
    
    Args:
        n (int): The number to be shifted.
        times (int): The number of positions to shift right.
    
    Returns:
        int: The result of shifting 'n' to the right by 'times' positions.
    """
    return n >> times

print(rightShift(3, 1))  # Output: 1


def bitwiseNot(n):
    """
    Performs a bitwise NOT operation.
    
    Args:
        n (int): The number to apply the NOT operation on.
    
    Returns:
        int: The result of applying the bitwise NOT on 'n'.
    """
    return ~n

print(bitwiseNot(3))  # Output: -4

def bitwiseXOR(a, b):
    """
    Performs a bitwise XOR operation between two numbers.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    
    Returns:
        int: The result of the bitwise XOR operation between 'a' and 'b'.
    """
    return a ^ b

# Example usage
print(bitwiseXOR(5, 3))  # Output: 6

def ifKthBitIsSetMethod1(n, k):
    """
    Checks if the k-th bit of the number n is set (i.e., 1).
    
    Args:
        n (int): The number to check.
        k (int): The bit position to check (1-based).
    
    Returns:
        bool: True if the k-th bit is set, False otherwise.
    """
    if (n & (1 << (k - 1))) != 0:
        return True
    else:
        return False

# Example usage
n, k = 5, 1
print(ifKthBitIsSetMethod1(n, k))  # Output: True (because the 1st bit of 5 (binary 101) is 1)

def ifKthBitIsSetMethod2(n, k):
    """
    Checks if the k-th bit of the number n is set (i.e., 1) using right shift.
    
    Args:
        n (int): The number to check.
        k (int): The bit position to check (1-based).
    
    Returns:
        bool: True if the k-th bit is set, False otherwise.
    """
    if ((n >> (k - 1)) & 1) == 1:
        return True
    else:
        return False

# Example usage
n, k = 13, 3
print(ifKthBitIsSetMethod2(n, k))  # Output: True (because the 3rd bit of 13 (binary 1101) is 1)

def countSetBitNaive(n):
    """
    Counts the number of set bits (1s) in the binary representation of 'n' using a naive approach.
    
    Args:
        n (int): The number to check.
    
    Returns:
        int: The number of set bits in the binary representation of 'n'.
    """
    res = 0
    while n > 0:
        if n % 2 != 0:  # Checks if the least significant bit is 1
            res += 1
        n = n // 2  # Right shift the number by one position (integer division by 2)
    return res

# Example usage
n = 13
print(countSetBitNaive(n))  # Output: 3 (13 in binary is 1101, which has three 1s)

def countSetBitbrianKerningamAlgo(n):
    """
    Counts the number of set bits (1s) in the binary representation of 'n' using the Brian Kernighan Algorithm.
    
    Args:
        n (int): The number to check.
    
    Returns:
        int: The number of set bits in the binary representation of 'n'.
    """
    res = 0
    while n > 0:
        n = n & (n - 1)  # Clears the least significant set bit
        res += 1
    return res

# Example usage
n = 13
print(countSetBitbrianKerningamAlgo(n))  # Output: 3 (13 in binary is 1101, which has three 1s)

def powerOf2Naive(n):
    """
    Determines if the given number 'n' is a power of 2 using a naive approach.
    
    Args:
        n (int): The number to check.
    
    Returns:
        bool: True if 'n' is a power of 2, False otherwise.
    """
    if n == 0:
        return False
    while n != 1:
        if n % 2 != 0:
            return False
        n //= 2  # Divide by 2
    return True

# Example usage
print(powerOf2Naive(8))   # Output: True (8 = 2^3)
print(powerOf2Naive(13))  # Output: False (13 is not a power of 2)

def powerOf2BrianKarningam(n):
    """
    Determines if the given number 'n' is a power of 2 using Brian Kernighan's algorithm.
    
    Args:
        n (int): The number to check.
    
    Returns:
        bool: True if 'n' is a power of 2, False otherwise.
    """
    if n == 0:
        return False
    return (n & (n - 1)) == 0

# Example usage
print(powerOf2BrianKarningam(8))   # Output: True (8 = 2^3)
print(powerOf2BrianKarningam(13))  # Output: False (13 is not a power of 2)

def findOdd(arr):
    """
    Finds the element that appears an odd number of times in the array.

    This function uses the XOR operation to find the element that appears an odd number 
    of times in the array. XOR has the property that x ^ x = 0 and x ^ 0 = x, which helps 
    in canceling out numbers that appear an even number of times.

    Args:
        arr (list): A list of integers where all elements except one appear an even number 
        of times. One element appears an odd number of times.

    Returns:
        int: The element that appears an odd number of times.

    Example:
        arr = [4, 3, 4, 4, 4, 5, 5]
        findOdd(arr)
        Output: 3
    """
    res = 0
    for i in arr:
        res = i ^ res  # XOR with res
    return res

arr = [4, 3, 4, 4, 4, 5, 5]
print(findOdd(arr))  # Output: 3

def findMissingNumber(arr):
    """
    Finds the missing number in an array containing numbers from 1 to n with one missing.

    This function uses XOR to find the missing number in the range from 1 to n, where 
    one number is missing from the array. The XOR of all numbers from 1 to n and the XOR 
    of all elements in the array will result in the missing number because x ^ x = 0 and 
    x ^ 0 = x.

    Args:
        arr (list): A list of integers containing numbers from 1 to n with one number missing.

    Returns:
        int: The missing number in the array.

    Example:
        arr = [1, 4, 3]
        findMissingNumber(arr)
        Output: 2
    """
    res = 0  # XOR of all numbers from 1 to n
    arrRes = 0  # XOR of all elements in the array
    n = len(arr) + 1  # The range of numbers from 1 to n (including the missing one)

    # XOR all the numbers from 1 to n
    for i in range(1, n + 1):
        res = res ^ i

    # XOR all the elements in the array
    for num in arr:
        arrRes = arrRes ^ num

    # The missing number is the XOR of res and arrRes
    return res ^ arrRes

arr = [1, 4, 3]
print(findMissingNumber(arr))  # Output: 2

def oddAppearing(arr):
    """
    Finds two elements in the array that appear an odd number of times.

    This function finds two numbers that appear an odd number of times in an array where 
    all other numbers appear an even number of times. It uses XOR to separate the numbers 
    based on the rightmost set bit.

    Steps:
    - XOR all the elements to get the XOR of the two odd-appearing numbers.
    - Find the rightmost set bit in the XOR result.
    - Separate the numbers based on the rightmost set bit and XOR them separately to find 
      the two odd-appearing numbers.

    Args:
        arr (list): A list of integers where exactly two numbers appear an odd number of times.

    Returns:
        tuple: A tuple containing the two numbers that appear an odd number of times.

    Example:
        arr = [3, 4, 3, 4, 5, 4, 4, 6, 7, 7]
        oddAppearing(arr)
        Output: (5, 6)
    """
    res1 = 0
    res2 = 0
    xor = 0
    
    # XOR all the elements to find XOR of the two odd appearing numbers
    for i in arr:
        xor = i ^ xor
    
    # Find the rightmost set bit in xor
    sn = xor & ~(xor - 1)
    
    # Separate the numbers into two groups and XOR them
    for i in range(0, len(arr)):
        if (arr[i] & sn) != 0:
            res1 = res1 ^ arr[i]
        else:
            res2 = res2 ^ arr[i]
    
    return res1, res2

arr = [3, 4, 3, 4, 5, 4, 4, 6, 7, 7]
print(oddAppearing(arr))  # Output: (5, 6)

def powerSet(s):
    """
    Generates all possible subsets (the power set) of a given string.

    This function computes the power set of a string by treating each character as a 
    bit in a binary number. It generates all possible subsets by iterating through 
    numbers from 0 to 2^n - 1 (where n is the length of the string) and using the 
    binary representation to determine whether a character is included in a subset.

    Args:
        s (str): The input string.

    Returns:
        list: A list containing all subsets (the power set) of the string.

    Example:
        s = "abc"
        powerSet(s)
        Output: ['', 'a', 'b', 'ab', 'c', 'ac', 'bc', 'abc']
    """
    n = len(s)
    p = pow(2, n)  # Total number of subsets (2^n)
    res = []
    
    # Loop through all numbers from 0 to 2^n - 1
    for i in range(p):
        subset = ""  # To store the current subset
        for j in range(n):
            if (i & (1 << j)) != 0:  # Check if the jth bit is set
                subset += s[j]
        res.append(subset)
    
    return res

s = "abc"
print(powerSet(s))  # Output: ['', 'a', 'b', 'ab', 'c', 'ac', 'bc', 'abc']
