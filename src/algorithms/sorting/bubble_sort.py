# 1. Go through list
# 2. Compare adjacent items, and swap if needed

# -- Set Up --
arr = [5, 3, 2, 4, 10, 1, 9]
n = len(arr)


# -- Bubble Sort Implementation --
for i in range(n - 1):
    swap_flag = False
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swap_flag = True
    if not swap_flag:
        break
