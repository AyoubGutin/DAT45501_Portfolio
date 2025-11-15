# -- Imports --
from typing import List


# -- Selection Sort Implementation
def selection_sort_func(arr: List) -> List:
    """
    Selection sort implementation

    1. Start the loop through the whole list
    2. Initialise the least index, starting at i
    3. Go through the list again from the least_index, and find the smallest element from the unsorted portion
    4. Repeat until list is sorted

    args:
        arr (List): The unsorted array

    return:
        arr (List): The sorted array
    """
    n = len(arr)
    for i in range(n):
        least_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[least_index]:
                least_index = j

        arr[i], arr[least_index] = arr[least_index], arr[i]

    return arr
