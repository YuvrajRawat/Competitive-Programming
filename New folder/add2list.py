def merge_list(list1, list2):
    result_list = list1 + list2
    return result_list

size1 = int(input())
list1 = [int(input()) for i in range(size1)]

size2 = int(input())
list2 = [int(input()) for i in range(size2)]

result = merge_list(list1, list2)

print(' '.join(map(str, result)))
