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

def insertArr(l, p, e):
    """
    Inserts an element at a specific position in a list.

    Args:
        l (list): The list to insert the element into.
        p (int): The position at which to insert the element.
        e (any): The element to be inserted.

    Returns:
        list: A new list with the element inserted at the specified position.
    """
    return l[:p] + [e] + l[p:]

l = [1, 2, 3, 4, 5]
p = 2
e = 5
print(insertArr(l, p, e))
