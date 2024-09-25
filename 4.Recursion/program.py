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
