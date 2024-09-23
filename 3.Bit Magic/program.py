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
