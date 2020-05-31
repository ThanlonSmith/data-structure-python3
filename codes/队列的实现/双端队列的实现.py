class Dqueue():
    def __init__(self):
        self.__list = []

    def add_tail(self, item):
        """
        从队列尾部添加元素
        :param item:
        :return:
        """
        self.__list.append(item)

    def remove_front(self):
        """
        从队列头部删除元素
        :return:
        """
        return self.__list.pop(0)

    def add_front(self, item):
        """
        从队列头部添加元素
        :param item:
        :return:
        """
        self.__list.insert(0, item)

    def remove_tail(self):
        """
        从队列尾部删除元素
        :param item:
        :return:
        """
        return self.__list.pop()

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)


# 创建一个空的双端队列
dq = Dqueue()
# 尾部添加元素，头部删除元素
dq.add_tail(1)
dq.add_tail(1.2)
dq.add_tail('thanlon')
dq.add_tail([1, 2, 3])
print('尾部已经完成元素的添加!')
print('当前队列是否为空：', dq.is_empty())
print('当前队列的大小：', dq.size())
print(dq.remove_front())
print(dq.remove_front())
print(dq.remove_front())
print(dq.remove_front())
# 尾部添加元素，头部删除元素
dq.add_front(1)
dq.add_front(1.2)
dq.add_front('thanlon')
dq.add_front([1, 2, 3])
print('头部已经完成元素的添加!')
print('当前队列是否为空：', dq.is_empty())
print('当前队列的大小：', dq.size())
print(dq.remove_tail())
print(dq.remove_tail())
print(dq.remove_tail())
print(dq.remove_tail())
"""
尾部已经完成元素的添加!
当前队列是否为空： False
当前队列的大小： 4
1
1.2
thanlon
[1, 2, 3]
头部已经完成元素的添加!
当前队列是否为空： False
当前队列的大小： 4
1
1.2
thanlon
[1, 2, 3]
"""