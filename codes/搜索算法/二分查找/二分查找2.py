def binary_search(alist, item):
    len_alist = len(alist)
    if len_alist == 0:
        return False
    else:
        middle_index = len_alist // 2
        if item == alist[middle_index]:
            return True
        elif item < alist[middle_index]:
            return binary_search(alist[:middle_index], item)
        else:
            return binary_search(alist[middle_index + 1:], item)


test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
print(binary_search(test_list, 3))
print(binary_search(test_list, 17))
"""
False
True
"""
