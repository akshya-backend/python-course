# Insertion Sort Algorithm in Python
# -----------------------------------
# Idea:
# Take one element at a time and insert it into
# the correct position in the sorted part.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Current element
        j = i - 1
        # Move elements greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# Example
data = [12, 11, 13, 5, 6]
print("Original array:", data)
sorted_data = insertion_sort(data)
print("Sorted array:", sorted_data)

"""
Step-by-step flow:
1. Start from second element (index 1).
2. Compare with elements in sorted part (left side).
3. Shift larger elements to the right.
4. Insert key into correct position.
5. Repeat until all elements are sorted.
"""
