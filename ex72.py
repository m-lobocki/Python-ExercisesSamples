# Please write a binary search function which searches an item in a sorted list. The function should return the index
# of element to be searched in the list.

def binary_search(list, item):
    left = 0
    right = len(list) - 1
    index = -1
    while right >= left and index == -1:
        middle = int((left + right) / 2)
        element = list[middle]
        if element < item:
            left = middle + 1
        elif element > item:
            right = middle - 1
        else:
            index = middle

    return index
