# def find_sum(arr):
#     t = int(input())
#     for i in range(len(arr)-1):
#         for j in range(i+1, len(arr)-1):
#             for k in range(j+1, len(arr)-1):
#                 if arr[i] + arr[j] + arr[k]== t:
#                     return i,j,k
#     return -1
            
# num = int(input())
# arr = list(map(int, input().split()))

# result = find_sum(arr)
# print(result)

def find(arr):
    t = int(input())
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)-1):
            for k in range (j+1, len(arr)-1):
                if arr[i] + arr[j] + arr[k] == t:
                    return i,j,k

num = int(input())
arr = list(map(int, input().split()))

result = find(arr)
print(result)

