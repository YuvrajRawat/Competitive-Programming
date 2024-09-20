def common(arr):
    for i in range(len(arr)-1):
        for j in range(i,len(arr)):
            if arr[j] == arr[i]:
                return j

arr = list(map(int, input().split(" ")))
result = common(arr)
print(result)    

# input_str = input("Enter space-separated numbers: ")
# arr = [int(num) for num in input_str.split() if num.isdigit()]
# result = common(arr)

# if result is not None:
#     print("First common element found at index:", result)
# else:
#     print("No common elements found.")

