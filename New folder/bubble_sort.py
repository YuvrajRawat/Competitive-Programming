def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage:
a = [35, 10, 31, 11, 26]
print("Before sorting, array elements are - ", a)
sorted_array = bubble_sort(a)
print("After sorting, array elements are - ", sorted_array)
