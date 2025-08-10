"""
Bubble Sort Algorithm in Python
--------------------------------
Idea:
Bubble Sort works by repeatedly swapping adjacent elements if they are in the wrong order.
This way, after each pass, the largest element "bubbles up" to the end.

Time Complexity:
- Worst case: O(n²) (when the list is in reverse order)
- Best case: O(n) (if the list is already sorted, with optimization)

Steps:
1. Compare arr[0] with arr[1]
2. If arr[0] > arr[1], swap them
3. Move to next pair, compare arr[1] with arr[2], and so on
4. After 1st pass, the largest element is at the last position
5. Repeat for remaining unsorted elements
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  # Number of passes
        swapped = False  # Optimization: stop if no swaps in a pass
        print(f"\nPass {i+1}:")
        for j in range(0, n-i-1):  # Compare up to last unsorted element
            print(f"  Comparing {arr[j]} and {arr[j+1]}...")
            if arr[j] > arr[j+1]:
                print(f"    Swapping {arr[j]} and {arr[j+1]}")
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap
                swapped = True
            else:
                print(f"    No swap needed")
        print(f"  Array after pass {i+1}: {arr}")
        if not swapped:
            break  # Stop if already sorted
    return arr


# Example usage
if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", nums)
    sorted_nums = bubble_sort(nums)
    print("\nFinal sorted array:", sorted_nums)
