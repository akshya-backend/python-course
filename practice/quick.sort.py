# Quick Sort Algorithm in Python
# -------------------------------
# Idea:
# Choose a pivot element.
# Partition array into elements less than pivot and greater than pivot.
# Recursively sort both parts.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Example
data = [10, 7, 8, 9, 1, 5]
print("Original array:", data)
sorted_data = quick_sort(data)
print("Sorted array:", sorted_data)

"""
Step-by-step flow:
1. Choose pivot (middle element here).
2. Create left list (elements < pivot),
   middle list (equal to pivot),
   right list (greater than pivot).
3. Recursively sort left and right lists.
4. Combine left + middle + right into final sorted array.
"""
