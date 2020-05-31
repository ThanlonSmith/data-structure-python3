def selection_sort(alist):
    n = len(alist)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if alist[j] < alist[min_index]:
                min_index = j
        # 判断当前最小值的索引是否还是i，如果是则i不用交换位置，否则需要交换位置
        if min_index != i:
            alist[i], alist[min_index] = alist[min_index], alist[i]


alist = [54, 226, 93, 17, 77, 31, 44, 55, 20]
selection_sort(alist)
print(alist)
"""
[17, 20, 31, 44, 54, 55, 77, 93, 226]
"""
