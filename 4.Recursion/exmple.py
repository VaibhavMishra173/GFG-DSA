def recFun(n):
    """
    A recursive function that prints numbers in a specific pattern.

    This function follows a recursive approach where it first makes a recursive call with 
    `n-1`, then prints the current value of `n`, and makes another recursive call with `n-1`. 
    It continues this process until `n` reaches 0, where it stops.

    Args:
        n (int): A positive integer to control the recursion depth.

    Example:
        recFun(3)
        Output:
        1
        2
        1
        3
        1
        2
        1
    """
    if n == 0:
        return
    recFun(n - 1)
    print(n)
    recFun(n - 1)

recFun(3)

def recFun2(n):
    """
    A recursive function that calculates the number of times a number can be divided by 2 before it becomes 1.

    This function recursively divides the input number `n` by 2 and counts how many divisions occur 
    until `n` becomes 1. This can also be interpreted as finding the number of times the input number 
    can be halved before reaching 1.

    Args:
        n (int): The input number, which should be greater than or equal to 1.

    Returns:
        int: The number of divisions by 2 performed until the number becomes 1.

    Example:
        recFun2(16)
        Output: 4 (because 16 -> 8 -> 4 -> 2 -> 1)
    """
    if n == 1:
        return 0
    return 1 + recFun2(n // 2)

print(recFun2(16))  # Output: 4
