def binary_search(alist, item):
    first_index = 0
    end_index = len(alist) - 1
    while end_index >= first_index:
        middle_index = (end_index + first_index) // 2
        if item == alist[middle_index]:
            return True
        elif item < alist[middle_index]:
            end_index = middle_index - 1
        else:
            first_index = middle_index + 1
    return False


test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
print(binary_search(test_list, 3))
print(binary_search(test_list, 17))
"""
False
True
