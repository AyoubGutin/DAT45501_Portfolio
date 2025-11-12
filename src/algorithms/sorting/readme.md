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

##
