def find_duplicates(arr):
    elements = []
    
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] and arr[i] not in elements:
                elements.append(arr[i])
    
    length = len(elements)
    return length

array = list(map(int, input().split()))

result = find_duplicates(array)
print(result)