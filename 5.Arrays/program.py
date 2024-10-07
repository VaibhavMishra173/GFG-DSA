def searchArr(l, e):
    """
    Searches for an element in a list.

    Args:
        l (list): The list to search in.
        e (any): The element to search for.

    Returns:
        bool: True if the element is found, False otherwise.
    """
    for ele in l:
        if ele == e:
            return True
    return False

l = [1, 2, 3, 4, 5]
print(searchArr(l, 5))
