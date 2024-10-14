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

def removeDuplicateFromSortedArrayEff(l):
    """
    Removes duplicates from a sorted array in place and returns the new length of the array.

    Args:
        l (list): A sorted list from which to remove duplicates.

    Returns:
        list: The same list with duplicates removed, truncated to the new length.
    """
    if not l:  # Check if the input list is empty
        return []

    res = 1  # Initialize a variable to track the position for unique elements
    for i in range(1, len(l)):
        if l[i] != l[i - 1]:  # Compare with the previous element
            l[res] = l[i]  # Place the unique element at the current position
            res += 1  # Move to the next position for the next unique element

    return l[:res]  # Return the modified list up to the new length

l = [1, 2, 3, 3, 4, 8, 8, 13]
print(removeDuplicateFromSortedArrayEff(l))  # Output: [1, 2, 3, 4, 8, 13]

def moveAllZeroToEnd(l):
    """
    Moves all zeros in the given list to the end while maintaining the order of non-zero elements.

    Args:
    l (list): A list of integers.

    Returns:
    list: A modified list where all zeros are moved to the end, and the order of non-zero elements is preserved.

    Example:
    >>> moveAllZeroToEnd([8, 5, 0, 10, 0, 20])
    [8, 5, 10, 20, 0, 0]
    """
    cnt = 0  # Counter for tracking position of non-zero elements
    for i in range(len(l)):
        if l[i] != 0:
            l[i], l[cnt] = l[cnt], l[i]  # Swap non-zero element with the element at 'cnt'
            cnt += 1  # Increment count for non-zero elements
    return l

l = [8, 5, 0, 10, 0, 20]
print(moveAllZeroToEnd(l))

def leftRotate(l):
    """
    Rotates the given list to the left by one position.

    Args:
    l (list): A list of elements.

    Returns:
    list: A modified list where all elements are shifted one position to the left, 
          and the first element is moved to the end of the list.

    Example:
    >>> leftRotate([1, 2, 3, 4, 5])
    [2, 3, 4, 5, 1]
    """
    res = l[1:]  # Slice the list from the second element to the end
    res.append(l[0])  # Append the first element to the end
    return res

l = [1, 2, 3, 4, 5]
print(leftRotate(l))

def leftRotateByD(l, d):
    """
    Rotates the given list to the left by 'd' positions.

    Args:
    l (list): A list of elements.
    d (int): The number of positions to rotate the list to the left.

    Returns:
    list: A modified list where all elements are shifted 'd' positions to the left,
          and the first 'd' elements are moved to the end.

    Example:
    >>> leftRotateByD([1, 2, 3, 4, 5], 2)
    [3, 4, 5, 1, 2]
    """
    res = l[d:]  # Slice the list from index 'd' to the end
    res.extend(l[0:d])  # Extend the list with the first 'd' elements
    return res

l = [1, 2, 3, 4, 5]
d = 2
print(leftRotateByD(l, d))

def findLeader(l):
    """
    Finds all the leaders in the list. A leader is an element that is greater than all the elements to its right.

    Args:
    l (list): A list of integers.

    Returns:
    list: A list of leaders in the order they are found.

    Example:
    >>> findLeader([7, 10, 4, 3, 6, 5, 2])
    [2, 5, 6, 10]
    """
    n = len(l)
    res = [l[n-1]]  # The last element is always a leader
    m = res[0]  # Initialize the max to the last element

    # Traverse the list from right to left
    for i in range(n-2, -1, -1):
        if l[i] > m:  # Compare current element with the max so far
            res.append(l[i])
            m = l[i]  # Update the max to the new leader
    
    return res[::-1]  # Reverse the result to maintain the original order

l = [7, 10, 4, 3, 6, 5, 2]
print(findLeader(l))

def maxDifferenceOfPair(l):
    """
    Finds the maximum difference between any two elements in the list where the larger element comes after the smaller one.

    Args:
    l (list): A list of integers.

    Returns:
    int: The maximum difference between any two elements where the larger element comes after the smaller element.

    Example:
    >>> maxDifferenceOfPair([2, 3, 10, 6, 4, 8, 1])
    8
    """
    # Initialize the result with the difference between the first two elements
    res = l[1] - l[0]
    minVal = l[0]  # Initialize the minimum value as the first element

    # Traverse the list starting from the second element
    for j in range(1, len(l)):
        # Update the result with the maximum difference found so far
        res = max(res, l[j] - minVal)
        # Update the minimum value encountered so far
        minVal = min(minVal, l[j])

    return res

l = [2, 3, 10, 6, 4, 8, 1]
print(maxDifferenceOfPair(l))
