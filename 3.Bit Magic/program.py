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
