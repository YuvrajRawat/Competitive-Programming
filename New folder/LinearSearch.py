def linear_search(array, x):
    for i in range(len(array)):
        if array[i] == x:
            return i
    return - 1

num = list(map(int,input("Enter the array Elements : ").split()))
target = int(input("Enter the target Element : "))

result = linear_search(num, target)

if result!= -1:
    print("Element present at index : ",str(result))
else:
    print("Element is not present")