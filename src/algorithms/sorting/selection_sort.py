# 1. Split list into sorted and unsorted
# 2. Append least elements into sorted list

arr = [5, 3, 2, 4, 10, 1, 9]
n = len(arr)

for i in range(n):
    least_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[least_index]:
            least_index = j

    arr[i], arr[least_index] = arr[least_index], arr[i]

print(arr)
