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

def deleteArr(l, e):
    """
    Deletes the first occurrence of an element from a list.

    Args:
        l (list): The list to remove the element from.
        e (any): The element to be removed.

    Returns:
        list: A new list with the element removed if it exists, otherwise the original list.
    """
    index = -1  # Initialize index to -1 to indicate element not found
    for i in range(len(l)):
        if l[i] == e:
            index = i
            break
    
    # If the element is found, return the list without the element
    if index >= 0:
        return l[:index] + l[index + 1:]
    
    # If the element is not found, return the original list
    return l

l = [1, 2, 6, 3, 4, 8]
e = 9
print(deleteArr(l, e))

def indexOfLargestEleInArr(l):
    """
    Finds the index of the largest element in the list.

    Args:
        l (list): The list to search through.

    Returns:
        int: The index of the largest element. If the list is empty, returns -1.
    """
    m = float('-inf')  # Initialize m to negative infinity
    ind = -1  # Initialize ind to -1 in case the list is empty
    
    for i in range(len(l)):
        if l[i] > m:
            m = l[i]
            ind = i
    
    return ind

l = [1, 9, 2, 6, 3, 4, 8]
print(indexOfLargestEleInArr(l))

def indexOfSecondLargestEleInArr(l):
    if len(l) < 2:
        return -1  # Return -1 if there are fewer than 2 elements

    m = float('-inf')  # Largest element
    snd = float('-inf')  # Second largest element
    ind = -1  # Index of largest element
    sndIdx = -1  # Index of second largest element

    for i in range(len(l)):
        if l[i] > m:
            # Update second largest before largest
            snd = m
            sndIdx = ind
            # Update largest
            m = l[i]
            ind = i
        elif l[i] > snd and l[i] != m:
            # Update second largest only if current element is not equal to largest
            snd = l[i]
            sndIdx = i
    
    return sndIdx

l = [1, 9, 2, 6, 3, 4, 8, 13]
print(indexOfSecondLargestEleInArr(l))  # Output: Index of second largest element
