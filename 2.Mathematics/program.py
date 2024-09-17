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

def findAllDivisorOfANumber(n):
    """
    Finds and prints all divisors of a given number n.

    This function iterates through all numbers from 1 to n and prints
    those that divide n evenly (i.e., the remainder is zero).

    Args:
        n (int): The integer whose divisors are to be found.

    Returns:
        None: The function prints all divisors of n.

    Example:
        findAllDivisorOfANumber(15)
        Output: 1, 3, 5, 15
    """
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
    return

findAllDivisorOfANumber(15)

def findAllDivisorsOfANumberOptimized(n):
    """
    This function finds and prints all divisors of a given number 'n'.
    It iterates up to the square root of 'n', printing both 'i' and 'n // i' when 'i' divides 'n'.

    Args:
    n (int): The number to find divisors of.

    Returns:
    None: The function prints each divisor of 'n'.
    
    Example:
    findAllDivisorsOfANumberOptimized(15) -> 1, 15, 3, 5
    """
    
    for i in range(1, int(n**0.5) + 1):  # Include sqrt(n) if it's an integer
        if n % i == 0:  # Check if i is a divisor
            print(i)  # Print the divisor
            if i != n // i:  # Check if n // i is a distinct divisor
                print(n // i)  # Print the corresponding larger divisor
    return

# Test the function
findAllDivisorsOfANumberOptimized(15)

def findAllDivisorsOfANumberFurtherOptimized(n):
    """
    Finds and prints all divisors of a given number n in an optimized way.

    This function iterates only up to the square root of n. For each divisor i found,
    it prints both i and n//i in separate loops. 

    Args:
        n (int): The integer whose divisors are to be found.

    Returns:
        None: The function prints all divisors of n.

    Example:
        findAllDivisorsOfANumberFurtherOptimized(15)
        Output: 1, 15, 3, 5
    """
    # First loop to find and print divisors up to sqrt(n)
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            print(i)
    
    # Second loop to find and print the complementary divisors
    for i in range(int(n ** 0.5), 0, -1):
        if n % i == 0:
            if i != n // i:
                print(n // i)

findAllDivisorsOfANumberFurtherOptimized(15)

def isNumberPrimeOptimized(n):
    """
    Determines if a number n is prime.

    This function checks if n is divisible by any number from 2 to the square root of n.
    If n is divisible by any such number, it returns False, meaning n is not prime. Otherwise, it returns True.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.

    Example:
        isNumberPrimeOptimized(7)
        Output: True
    """
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def printPrimes(n):
    """
    Prints all prime numbers up to n.

    This function iterates through all numbers from 2 to n and uses the isNumberPrimeOptimized function
    to check if each number is prime. If a number is prime, it prints the number.

    Args:
        n (int): The upper limit (inclusive) for printing prime numbers.

    Returns:
        None: The function prints all prime numbers up to n.

    Example:
        printPrimes(10)
        Output: 2, 3, 5, 7
    """
    for i in range(2, n + 1):
        if isNumberPrimeOptimized(i):
            print(i)
    return

printPrimes(10)

def printPrimesSieveAlgo(n):
    """
    Prints all prime numbers up to n using the Sieve of Eratosthenes algorithm.

    This function creates a boolean list where indices represent numbers from 0 to n.
    It marks non-prime numbers as False, starting from 2, and for each prime i, it marks
    all its multiples as non-prime. Finally, it prints all numbers that are still marked as prime.

    Args:
        n (int): The upper limit (inclusive) for printing prime numbers.

    Returns:
        None: The function prints all prime numbers up to n.

    Example:
        printPrimesSieveAlgo(10)
        Output: 2, 3, 5, 7
    """
    lst = [True] * (n + 1)
    for i in range(2, int(n**0.5) + 1):
        if lst[i]:
            for j in range(2 * i, n + 1, i):
                lst[j] = False
    for i in range(2, n + 1):
        if lst[i]:
            print(i)
    return

printPrimesSieveAlgo(10)

def printPrimesSieveAlgoOptimized(n):
    """
    Prints all prime numbers up to n using an optimized version of the Sieve of Eratosthenes algorithm.

    This function marks non-prime numbers in a boolean list. Starting from 2, for each prime number i, 
    it marks all its multiples as non-prime, starting from i * i (to avoid redundant checks for smaller numbers). 
    After processing, all prime numbers up to n are printed.

    Args:
        n (int): The upper limit (inclusive) for printing prime numbers.

    Returns:
        None: The function prints all prime numbers up to n.

    Example:
        printPrimesSieveAlgoOptimized(10)
        Output: 2, 3, 5, 7
    """
    lst = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if lst[i]:
            for j in range(i * i, n + 1, i):
                lst[j] = False
    for i in range(2, n + 1):
        if lst[i]:
            print(i)
    return

printPrimesSieveAlgoOptimized(10)

def printPrimesSieveAlgoOptimizedShort(n):
    """
    Prints all prime numbers up to n using a short and optimized version of the Sieve of Eratosthenes algorithm.

    This function iterates through numbers from 2 to n. For each prime number i, it prints i and marks all 
    its multiples starting from i * i as non-prime. 

    Args:
        n (int): The upper limit (inclusive) for printing prime numbers.

    Returns:
        None: The function prints all prime numbers up to n.

    Example:
        printPrimesSieveAlgoOptimizedShort(10)
        Output: 2, 3, 5, 7
    """
    lst = [True] * (n + 1)
    for i in range(2, n + 1):
        if lst[i]:
            print(i)
            for j in range(i * i, n + 1, i):
                lst[j] = False
    return

printPrimesSieveAlgoOptimizedShort(10)

def computePower(x, n):
    """
    Computes the power of a number x raised to the exponent n.

    This function iterates from 1 to n, multiplying the result by x in each iteration 
    to compute the power. It calculates x^n (x raised to the power of n).

    Args:
        x (int or float): The base number.
        n (int): The exponent (the number of times to multiply the base).

    Returns:
        int or float: The result of x raised to the power n.

    Example:
        computePower(3, 4)
        Output: 81 (since 3^4 = 81)
    """
    result = 1
    for i in range(1, n + 1):
        result = result * x
    return result

print(computePower(3, 4))  # Output: 81

def computePowerOptimized(x, n):
    """
    Computes the power of a number x raised to the exponent n using an optimized approach.

    This function uses a recursive approach to calculate x^n. It leverages the property that:
    - x^n = (x^(n//2))^2 when n is even
    - x^n = x * (x^(n//2))^2 when n is odd

    This reduces the time complexity from O(n) in the iterative approach to O(log n).

    Args:
        x (int or float): The base number.
        n (int): The exponent (the number of times to multiply the base).

    Returns:
        int or float: The result of x raised to the power n.

    Example:
        computePowerOptimized(3, 5)
        Output: 243 (since 3^5 = 243)
    """
    if n == 0:
        return 1
    temp = computePowerOptimized(x, n // 2)
    temp *= temp
    if n % 2 == 0:
        return temp
    else:
        return temp * x

print(computePowerOptimized(3, 5))  # Output: 243
