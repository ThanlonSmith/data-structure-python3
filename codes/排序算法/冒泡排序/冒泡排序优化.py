def bubble_sort(alist):
    n = len(alist)
    for i in range(n - 1, 0, -1):
        count = 0
        for j in range(i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                count += 1
        if count == 0:
            return
    return alist

test_list = [9, 2, 3, 3, 1, 0]
bubble_sort(test_list)
print(test_list)
"""
[0, 1, 2, 3, 3, 9]
"""
