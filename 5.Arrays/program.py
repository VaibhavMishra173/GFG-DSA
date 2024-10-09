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

def isSorted(l):
    """
    Checks if the list is sorted in ascending order.

    Args:
        l (list): The list to check.

    Returns:
        bool: True if the list is sorted in ascending order, False otherwise.
    """
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False  # As soon as we find an out-of-order element, return False
    return True  # If no out-of-order elements are found, return True

l = [1, 9, 2, 6, 3, 4, 8, 13]
l1 = [1, 2, 3, 4, 8]
print(isSorted(l))   # Output: False
print(isSorted(l1))  # Output: True


def reverseNaive(l):
    """
    Reverses the input list.

    Args:
        l (list): The list to reverse.

    Returns:
        list: A new list with the elements in reverse order.
    """
    res = []
    for i in range(len(l) - 1, -1, -1):  # Loop correctly from len(l)-1 to 0
        res.append(l[i])
    return res

l = [1, 9, 2, 6, 3, 4, 8, 13]
print(reverseNaive(l))  # Output: [13, 8, 4, 3, 6, 2, 9, 1]

def reverse(l):
    """
    Reverses the input list in place.

    Args:
        l (list): The list to reverse.

    Returns:
        list: The same list with its elements reversed in place.
    """
    low = 0
    high = len(l) - 1
    
    # Swap elements from the start and end moving towards the middle
    while low < high:
        l[low], l[high] = l[high], l[low]
        low += 1
        high -= 1
    
    return l

l = [1, 9, 2, 6, 3, 4, 8, 13]
print(reverse(l))  # Output: [13, 8, 4, 3, 6, 2, 9, 1]

def removeDuplicateFromSortedArray(l):
    """
    Removes duplicates from a sorted array.

    Args:
        l (list): A sorted list from which to remove duplicates.

    Returns:
        list: A new list containing only unique elements from the input list.
    """
    if not l:  # Check if the input list is empty
        return []

    uniq = [l[0]]  # Initialize with the first element
    for i in range(1, len(l)):
        if uniq[-1] != l[i]:  # Compare with the last unique element
            uniq.append(l[i])  # Add unique element to the list
            
    return uniq

l = [1, 2, 3, 3, 4, 8, 8, 13]
print(removeDuplicateFromSortedArray(l))  # Output: [1, 2, 3, 4, 8, 13]
