from random import shuffle


def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    mid = len(alist) // 2
    left = alist[:mid]
    right = alist[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))


def merge(left, right):
    sorted_list = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1
    if left:
        sorted_list.extend(left[left_index:])
    if right:
        sorted_list.extend(right[right_index:])
    return sorted_list


array = list(range(30))
shuffle(array)

print(merge_sort(array))
