def findPrimeFactorsOptimized(n):
    """
    Finds and prints the prime factors of a given number n.

    This function optimizes the process by only iterating up to the square root of n.
    For each factor found, it continuously divides n by that factor until n is no longer divisible.
    The remaining n is either 1 or a prime number, which is appended to the result.

    Args:
        n (int): The integer whose prime factors are to be found.

    Returns:
        None: The function prints the list of prime factors.

    Example:
        findPrimeFactorsOptimized(450)
        Output: [2, 3, 3, 5, 5]
    """
    array = []
    if n <= 1:
        return
    for number in range(2, int(n ** 0.5) + 1):
        while n % number == 0:
            array.append(number)
            n = n / number
    if n > 1:
        array.append(n)
    print(array)

findPrimeFactorsOptimized(450)
findPrimeFactorsOptimized(84) #Edge case, use last if condition


def findPrimeFactorsFurtherOptimized(n):
    """
    This function finds and prints the prime factors of a given number 'n'.
    It uses an optimized approach to first remove factors of 2 and 3,
    then checks for other prime factors starting from 5 and beyond, using 6k ± 1 rule.
    
    Args:
    n (int): The number to find prime factors of.

    Returns:
    None: The function prints the list of prime factors of 'n'.
    
    Example:
    findPrimeFactorsFurtherOptimized(450) -> [2, 3, 3, 5, 5]
    findPrimeFactorsFurtherOptimized(84) -> [2, 2, 3, 7]
    """
    
    lst = []
    if n <= 1:
        return
    
    # Remove all factors of 2
    while n % 2 == 0:
        lst.append(2)
        n //= 2
    
    # Remove all factors of 3
    while n % 3 == 0:
        lst.append(3)
        n //= 3
    
    # Check for other prime factors starting from 5 and 5 + 2 (i.e., 7)
    for number in range(5, int(n**0.5) + 1, 6):
        while n % number == 0:
            lst.append(number)
            n //= number
        while n % (number + 2) == 0:
            lst.append(number + 2)
            n //= (number + 2)
    
    # If n is still greater than 3, it must be prime
    if n > 3:
        lst.append(n)
    
    print(lst)

# Test the function
findPrimeFactorsFurtherOptimized(450)
findPrimeFactorsFurtherOptimized(84)

