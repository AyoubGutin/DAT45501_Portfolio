# -- Imports --
from typing import List


# -- Bubble Sort Implementation --
def bubble_sort_func(arr: List) -> List:
    """
    Bubble sort implementation

    1. go through the whole  except from last item, as unecessary, using the outer loop. The intial list is the unsorted portion, which shrinks by 1 after each pass
    2. in the inner loop, go through the unsorted portion, and swap if adjacent items need to do so
    3. for a pass, if no swaps are made, finish the sort

    args:
        arr [List]: The array / list to be sorted

    return:
        arr (List): The sorted array / list
    """
    n = len(arr)
    for i in range(n - 1):
        swap_flag = False
        # the unsorted portion decreases after every pass
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_flag = True
        if not swap_flag:
            break

    return arr
