def largest(arr):
    arr.sort()
    return arr[-1]


num = int(input())
arr = list(map(int, input().split(" ")))

result = largest(arr)
print(result)

