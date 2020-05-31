def insert_sort(alist):
    for i in range(1, len(alist)):
        for j in range(i, 0, -1):
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]
            """
            # 最优时间复杂度的情况
            else:
                break
            """

alist = [6, 5, 3, 1, 8, 7, 2, 4, ]
insert_sort(alist)
print(alist)
"""
[1, 2, 3, 4, 5, 6, 7, 8]
"""
