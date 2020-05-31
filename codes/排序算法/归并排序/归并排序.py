def merger_sort(alist):
    # 每次都要获取分组后列表的长度
    n = len(alist)
    # 根据列表的长度分组
    mid_elem = n // 2
    # 当列表只有一个元素时无法分组就直接返回这个列表
    if n <= 1:
        return alist
    # 分组后左边的元素形成的新列表
    left_elems = merger_sort(alist[:mid_elem])
    # 分组之后右边的元素形成的新列表
    right_elems = merger_sort(alist[mid_elem:])
    # 左右列表分别设置一个指针
    left_pointer, right_pointer = 0, 0
    # 新的列表用于存放需要合并的且排序好的左右子列表
    ret = []
    # 只要指针的值小于左右子列表的长度，需要继续排序
    while left_pointer < len(left_elems) and right_pointer < len(right_elems):
        # 如果左子列表的元素小于或者等于右子列表则将左子列表的该元素添加到新列表中，指针向后移动1次
        if left_elems[left_pointer] <= right_elems[right_pointer]:
            ret.append(left_elems[left_pointer])
            left_pointer += 1
        # 如果右子列表的元素小于或者等于左子列表则将右子列表的该元素添加到新列表中，指针向后移动一次
        else:
            ret.append(right_elems[right_pointer])
            right_pointer += 1
    # 剩下的元素直接追加到列表后面，比如1，2，3，4排好1，2剩下的3，4直接追加到列表中
    # 这里由于执行效率的原因不建议使用列表相加
    ret.extend(left_elems[left_pointer:])
    ret.extend(right_elems[right_pointer:])
    return ret


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
sorted_alist = merger_sort(alist)
print(sorted_alist)
"""
[17, 20, 26, 31, 44, 54, 55, 77, 93]
"""
