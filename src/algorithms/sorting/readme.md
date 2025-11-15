# Sorting Algorithms

## Bubble Sort

`bubble_sort.py`

- Bubble sort is a sorting algorithm that loops through the list element by element, comparing the current value with the one after it.
- Passes through the list are made until no swaps happen for that swap

- Very inefficient in real life
- Worst and average case: O(n^2)
- Best case: O(n) - when a list is already sorted

Elements that must move towards the end of the list are considered rabbits, as it is quicker for them to be sorted due to wins of successive swaps.

In comparison, elements that move towards the beginning would be more slower as it canot move faster than one step per pass. They are considered turtle elements.

## Selection Sort

`selection_sort.py`

- Selection sort esentially finds the lowest/highest element in a list/array from the unsorted portion and moves it to the front of the list/array, depending on if you ascending/descending
- The unsorted portion gets smaller as items go on the front list, it starts an index 0, then moves up incrementally
- It is an in-place sort, so it directly operates on the array

## Insertion Sort

`insertion_sort.py`

- Insertion sort grows a sorted list by looping through the list and inserting each element of the unsorted list into its correct position in a sorted portion of the list
- Start with the second element, as first is assumed to be sorted
- Compare the second element, with the first, and swap if needed
- Go to the next element, compare with the sorted portion, and repeat
