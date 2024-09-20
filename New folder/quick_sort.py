# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[-1]
#         left = [x for x in arr[:-1] if x < pivot]
#         middle = [ x for  x in arr if x == pivot]
#         right = [x for x in arr[:-1] if x > pivot]
         
#     return quick_sort(left) + middle + quick_sort(right)

# # Example usage:
# arr = [10, 7, 8, 9, 1, 5]
# sorted_arr = quick_sort(arr)
# print("Sorted array:", sorted_arr)

def quick_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    else:
        pivot = arr[-1]
        left = [x for x in arr[:-1] if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr[:-1] if x > pivot]
        
    return quick_sort(left) + middle +quick_sort(right)

arr = [1,3,2,4,9,8,5,7,6]
result = quick_sort(arr)
print(result)