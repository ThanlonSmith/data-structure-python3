def bubble_sort(alist):
    n = len(alist)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
    return alist


test_list = [9, 2, 3, 3, 1, 0]
bubble_sort(test_list)
print(test_list)
"""
[0, 1, 2, 3, 3, 9]
"""
