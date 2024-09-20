# def max_sum_subarray(nums, k):

#     max_sum = sum(nums[:k])  # Initialize max_sum with the sum of first k elements
#     current_sum = max_sum

#     for i in range(k, len(nums)):
#         current_sum += nums[i] - nums[i - k]  # Slide the window

#         max_sum = max(max_sum, current_sum)

#     return max_sum

# # Example usage:
# nums = list(map(int, input().split(",")))
# k = 3
# print("Maximum sum of subarray of size", k, "is:", max_sum_subarray(nums, k))


# def max_subarray(arr, k):
    
#     current_sum = sum(arr[:3])
#     max_sum = current_sum

#     for i in range(3, len(arr)):
#         current_sum += arr[i] - arr[i-k]
#         max_sum = max(current_sum,max_sum)

#     return max_sum
# arr = list(map(int, input().split(",")))
# k = 3
# result = max_subarray(arr,k)
# print(result)

def two_sum(arr, k):
    result = []
    seen = set()  # Keep track of seen elements to avoid duplicates
    
    for i in range(len(arr)):
        complement = k - arr[i]
        if complement in seen:
            result.append((arr.index(complement), i))
        seen.add(arr[i])
    
    return result

# Example usage:
arr = list(map(int, input("Enter the array elements separated by commas: ").split(",")))
k = int(input("Enter the target sum: "))

result = two_sum(arr, k)
print("Indices pairs with sum equal to", k, ":", result)
