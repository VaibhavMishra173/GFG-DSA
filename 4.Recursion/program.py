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
