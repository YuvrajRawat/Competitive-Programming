def find_smallest_largest(arr):
    smallest = float('inf')
    largest = float('-inf')

    for num in  arr:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    
    return smallest,largest

n = int(input("Enter the size of array: "))
arr = list(map(int,input().split()))

smallest, largest = find_smallest_largest(arr)

print(smallest)
print(largest)