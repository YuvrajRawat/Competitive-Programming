def duplicate_arr(arr):
    duplicate = []

    arr.sort()

    for i in range (1,len(arr)):
        if arr[i-1] == arr[i]:
            duplicate.append(arr[i])
    
    return duplicate



arr = [1,2,9,8,9,7,5,4,7,6,5,4,6]
result = duplicate_arr(arr)
print(result)