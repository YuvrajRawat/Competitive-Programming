def zero(arr):
    zero_arr = []
    element_arr = []

    for i in range(len(arr)):
        if arr[i] == 0:
            zero_arr.append(arr[i])

    for i in range(len(arr)):
        if arr[i] != 0:
            element_arr.append(arr[i])

    addition = element_arr + zero_arr

    return addition

arr = [1,3,5,6,7,0,2,0,5,0,7,8]
result = zero(arr)
print(result)

# def zero(arr):
#     zero_arr = []
#     element_arr = []

#     # Iterate over each element in the input array
#     for i in range(len(arr)):
#         if arr[i] == 0:
#             zero_arr.append(arr[i])
#         else:
#             element_arr.append(arr[i])

#     # Combine the element_arr (non-zero elements) with zero_arr (zero elements)
#     addition = element_arr + zero_arr

#     return addition

# arr = [1, 3, 5, 6, 7, 0, 2, 0, 5, 0, 7, 8]
# result = zero(arr)
# print(result)  # Output should be: [1, 3, 5, 6, 7, 2, 5, 7, 8, 0, 0, 0]
