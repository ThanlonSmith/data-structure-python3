def shell_sort(alist):
    n = len(alist)
    # 如果是9个元素，则gap从4开始(不能确定取半才能是最优的)
    gap = n // 2
    # gap最小缩小为1，也就是不能大于0
    while gap > 0:
        for i in range(gap, n):
            for i in range(i, 0, -gap):
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
            """
            # 与内层的for循环是等价的
            while i > 0:
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                i -= gap
            """

        # 缩短gap
        gap //= 2

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(alist)
print(alist)
"""
[17, 20, 26, 31, 44, 54, 55, 77, 93]
"""
