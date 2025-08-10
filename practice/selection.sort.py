# Selection Sort Algorithm in Python
# -----------------------------------
# Idea:
# Find the smallest element in the unsorted part,
# place it at the beginning.
# Repeat for all positions.

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the first unsorted element is the minimum
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap found minimum with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example
data = [64, 25, 12, 22, 11]
print("Original array:", data)
sorted_data = selection_sort(data)
print("Sorted array:", sorted_data)

"""
Step-by-step flow:
1. Select the smallest element from the unsorted list.
2. Swap it with the first element of unsorted part.
3. Move boundary forward by 1 and repeat.
4. Continue until all elements are sorted.
"""
