def rotate(arr, operation):

    n = len(arr)
    direction = operation[0]
    k = int(operation[1:])

    if direction == 'L':
        left = arr[:k]
        right = arr[k:]

        new_arr = right + left
    
    elif direction == 'R':
        left = arr[:-k]
        right = arr[-k:]

        new_arr = right + left

    return new_arr


arr = list(map(int, input().split(",")))

operation = input()

result = rotate(arr, operation)

print(result)