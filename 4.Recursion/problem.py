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

# Mapping of digits to corresponding letters on a phone keypad
keypad = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz"
}

def possibleWords(a, N):
    """
    Generates all possible words from the given array of phone digits.
    
    Parameters:
    a (list of int): Array representing the phone digits.
    N (int): The length of the array.

    Returns:
    list of str: A list containing all possible words formed from the digits.
    """
    # List to store the results
    result = []
    
    # Helper function to perform recursive backtracking
    def backtrack(index, current_word):
        # Base case: If the current_word has N letters, add it to the result
        if index == N:
            result.append(current_word)
            return
        
        # Get the corresponding letters for the current digit
        letters = keypad[a[index]]
        
        # For each letter, continue building the word recursively
        for letter in letters:
            backtrack(index + 1, current_word + letter)
    
    # Start the backtracking process from the first digit
    backtrack(0, "")
    
    # Return the result list in lexicographical order
    return sorted(result)


# Example test cases
a = [2, 3, 4]
N = len(a)
print(possibleWords(a, N))
# Output: ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi', 'bdg', 'bdh', 'bdi', 'beg', 'beh', 'bei', 'bfg', 'bfh', 'bfi', 'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi']

a = [3, 4, 5]
N = len(a)
print(possibleWords(a, N))
# Output: ['dgj', 'dgk', 'dgl', 'dhj', 'dhk', 'dhl', 'dij', 'dik', 'dil', 'egj', 'egk', 'egl', 'ehj', 'ehk', 'ehl', 'eij', 'eik', 'eil', 'fgj', 'fgk', 'fgl', 'fhj', 'fhk', 'fhl', 'fij', 'fik', 'fil']
