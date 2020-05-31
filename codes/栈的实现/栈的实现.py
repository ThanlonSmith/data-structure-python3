class Stack():
    def __init__(self):
        self.__items = []  # 不希望操作栈的人直接操作内部容器：可以绕过push和pop，直接对头尾操作

    def push(self, item):
        """
        压栈:添加一个新元素item到栈顶
        :param item: 压入栈顶的元素
        :return:
        """
        # self.__items.insert(0,item)
        self.__items.append(item)

    def pop(self):
        """
        出栈：弹出栈顶元素
        :return:弹出的元素
        """
        # self.__items.pop(0)
        return self.__items.pop()

    def peek(self):
        """
        返回栈顶元素
        :return:
        """
        return self.__items[-1] if self.__items else None

    def is_empty(self):
        """
        判断栈是否为空
        :return: True or False
        """
        # return self.__items == []
        return not self.__items

    def size(self):
        """
        返回栈的大小
        :return:
        """
        return len(self.__items)


if __name__ == '__main__':
    s = Stack()
    print('压栈...')
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print('当前栈的元素数：', s.size())
    print('出栈...')
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print("当前栈为%s栈！" % '空' if s.is_empty() else '非空')
    print('当前栈的元素数：{0}个'.format(s.size()))
"""
压栈...
当前栈的元素数： 4
出栈...
4
3
2
1
当前栈为空栈！
当前栈的元素数：0个
"""
