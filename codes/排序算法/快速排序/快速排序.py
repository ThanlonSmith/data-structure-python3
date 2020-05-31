def quick_sort(alist, first, last):
    # 递归结束条件
    if first >= last:
        return
    # 基准值
    pivot_value = alist[first]
    # 每次传入的索引位置：first和last都是不同的
    low_pointer = first
    high_pointer = last
    while low_pointer < high_pointer:
    	# 当列表中高索引位置的元素大于或者等于基准值时，只需要索引-1，也就是索引移动到上一个元素
        while low_pointer < high_pointer and alist[high_pointer] >= pivot_value:
            high_pointer -= 1
        # 当存在小于基准值的元素，while循环停止，索引移动停止，把这个索引放到低索引位置
        alist[low_pointer] = alist[high_pointer]
        # 当列表中低索引位置的元素小于基准值时，只需要低索引+1，也就是移动到下一个元素
        while low_pointer < high_pointer and alist[low_pointer] <= pivot_value:
            low_pointer += 1
        # 当存在大于基准值的元素，while循环停止，索引移动停止，把这个索引放到高索引位置
        alist[high_pointer] = alist[low_pointer]
    # low_pointer也可以换成high_pointer，因为这个时候low_pointer与high_pointer是等价的
    alist[low_pointer] = pivot_value
    # low_pointer左边的列表进行快速排序
    quick_sort(alist, first, low_pointer - 1)
    # low_pointer右边的列表进行快速排序
    quick_sort(alist, low_pointer + 1, last)

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(alist, 0, len(alist) - 1)
print(alist)
"""
[17, 20, 17, 17, 31, 54, 17, 17, 93]
"""
