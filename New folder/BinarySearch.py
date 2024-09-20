
# def binary_search(array, x):
#     left = 0
#     right = len(array) - 1

#     while left <= right:
#         mid = (left + right) // 2
#         if array[mid] > x:
#             right = mid - 1
#         elif array[mid] < x:                   
#             left = mid + 1
#         else:
#             return mid 
#     return -1

# num = list(map(int,input("Enter the array Elements : ").split()))
# target = int(input("Enter the target Element : "))

# result = binary_search(num, target)

# if result!= -1:
#     print("Element present at index : ",str(result))
# else:
#     print("Element is not present")
def bs(arr, k):
    left = 0
    right = len(arr)-1
    
    mid = (right + left)//2
    while left <= right:
        if arr[mid] > k:
            right = mid -1
        elif arr[mid] < k:
            left = mid + 1
        else:
            return mid
            
    return -1
    
arr = [1,2,3,5,6,8,9]
k = 8

result = bs(arr, k)
print(str(result))