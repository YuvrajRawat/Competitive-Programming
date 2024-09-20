arr = [1,7,2,9,6,2,4,3,6,5]

def unique_ele(arr):
    
    unique = []
    
    for i in range(1,len(arr)-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            unique.append(arr[i])
    
    return unique

result = unique_ele(arr)
print(result)