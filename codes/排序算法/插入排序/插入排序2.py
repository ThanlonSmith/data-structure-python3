def insert_sort(alist):
    for i in range(1, len(alist)):
        while i > 0:
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
            # 最优时间复杂度的情况
            # else:
            #     break
            i -= 1

alist = [6, 5, 3, 1, 8, 7, 2, 4, ]
insert_sort(alist)
print(alist)
"""
[1, 2, 3, 4, 5, 6, 7, 8]
"""
