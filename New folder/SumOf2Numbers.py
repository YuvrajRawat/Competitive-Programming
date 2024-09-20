# def find_sum(arr):
#     k = int(input())
#     for i in (0,len(arr)):
#         for j in range(1,len(arr)):
#             if arr[i] + arr[j] == k:
#                 return 1
#             else:
#                 return -1
            
# num = int(input())
# arr = list(map(int,input().split()))

# result = find_sum(arr)
# print(result)

def find_sum(arr):
    k = int(input())
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == k:
                return 1
    return -1
            
num = int(input())
arr = list(map(int, input().split()))

result = find_sum(arr)
print(result)


# def find_sum(arr, k):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] + arr[j] == k:
#                 return "Yes"
#     return "No"

# num_tests = int(input())

# for _ in range(num_tests):
#     size, target = map(int, input().split())
#     array = list(map(int, input().split()))

#     result = find_sum(array, target)
#     print(result)


# output
# 2 test case
# 5 31
# 10 11 13 17 21
# 5 44
# 10 11 13 17 21