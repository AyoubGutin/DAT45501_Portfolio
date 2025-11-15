# -- Imports --
from typing import List


# -- Insertion Sort Implementation --
def insertion_sort_func(arr: List) -> List:
    """
    Insertion sort implementation

    1. Start the loop through the whole list
    2. Store the current value for easier access
    3. Initialise j, which is always 1 behind i, this is the 'sorted' portion
    4. Using a while loop, if the value at index j is larger than the current value, shift j by 1. Repeat until j is smaller, or j is at the start.
    5. Put the current value in the gap (j + 1)

    args:
        arr (List): The array/list to be sorted

    return:
        arr (List): The sorted array/lisr
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]  # store the current value
        j = (
            i - 1
        )  # the end of the boundary/sorted portion to be considered (0 to i - 1)
        while j >= 0 and arr[j] > key:
            # increment downards of the sorted portion, shifting the larger elements to the right, until either j is at the start of the list or j is smaller than the current value
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # put the current value in the gap

    return arr
