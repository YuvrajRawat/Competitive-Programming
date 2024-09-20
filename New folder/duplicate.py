# # def find_duplicate(nums):
# #     nums.sort()
# #     duplicates = []

# #     for i in range(1, len(nums)):
# #         if nums[i] == nums[i - 1]:
# #             duplicates.append(nums[i])

# #     return duplicates

# # # Example usage:
# # numbers = list(map(int,input().split(",")))
# # result = find_duplicate(numbers)

# # if result:
# #     print("Duplicate numbers:", ", ".join(map(str,result)))
# # else:
# #     print("No duplicates found.")


# def find_duplicates(arr):

#     arr.sort()
#     duplicates = []
    
#     for i in range (1, len(arr)):
#         if arr[i] == arr[i-1]:
#             duplicates.append(arr[i])

#     return duplicates

# arr = list(map(int, input().split(",")))
# result = find_duplicates(arr)
# print(",".join(map(str, result)))

def find_duplicate(arr):
    arr.sort()
    duplicates = []

    for i in range(1,len(arr)-1):
        if arr[i] == arr[i-1]:
            duplicates.append(arr[i])
    
    return duplicates
arr = [1,1,2,3,4,4,5]
result = find_duplicate(arr)

print(" ".join(map(str, result)))

        