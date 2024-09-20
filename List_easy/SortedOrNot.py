def largest(arr):
    new_arr = sorted(arr)

    if new_arr == arr:
        return "Yes"
    else:
        return "No"

num = int(input())
arr = list(map(int, input().split(" ")))

result = largest(arr)
print(result)

