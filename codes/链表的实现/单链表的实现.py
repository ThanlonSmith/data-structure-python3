class SingleNode:
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SimpleLinkedList:
    """
    单向链表
    """

    def __init__(self, node=None):
        """
        :param node:默认是空链表
        """
        self.__head = node

    def is_empty(self):
        """
        判断是否为空
        :return:
        """
        return self.__head is None

    def length(self):
        """
        链表的长度
        :return:count
        """
        # 如果是空链表直接就返回count=0
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """
        遍历链表
        :return:
        """
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=' ')
            cur = cur.next

    def add(self, elem):
        """
        从链表的头部添加元素
        :param elem:
        :return:
        """
        node = SingleNode(elem)
        """
        # 下面也可以处理是空链表的情况
        if self.is_empty():
            self.__head = node
        node.next = self.__head
        """
        node.next = self.__head
        self.__head = node

    def append(self, elem):
        """
        尾部添加元素
        :param elem:
        :return:
        """
        node = SingleNode(elem)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, elem):
        node = SingleNode(elem)
        if pos <= 0:
            self.add(elem)
            return
        elif pos > self.length() - 1:
            self.append(elem)
            return
        pre = self.__head
        count = 0
        while count < pos - 1:
            pre = pre.next
            count += 1
        node.next = pre.next
        pre.next = node

    def search(self, elem):
        """
        查找元素
        :param self:
        :param elem:
        :return:
        """
        # 也可以处理空链表的情况
        cur = self.__head
        while cur is not None:
            if cur.elem == elem:
                return True
            else:
                cur = cur.next
        return False

    def remove(self, elem):
        pre = None
        cur = self.__head
        # 适用于空节点和删除头节点
        while cur is not None:
            if cur.elem == elem:
                # 判断当前节点是否是头节点
                # 也可以解决链表中只有一个头节点
                if cur == self.__head:
                    self.__head = self.__head.next
                    # self.__head = cur.next
                else:
                    # 也适用于删除尾部节点
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next


sll = SimpleLinkedList()
print('当前链表是否为空：', sll.is_empty())
print('当前链表长度：', sll.length())
print('------在链表尾部添加节点------')
sll.append(1)
print('当前链表是否为空：', sll.is_empty())
print('当前链表长度：', sll.length())
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(5)
sll.append(6)
print('当前链表是否为空：', sll.is_empty())
print('当前链表长度：', sll.length())
print('遍历链表：', end='')
sll.travel()
print('\n------在链表头部添加节点-----')
sll.add(7)
print('当前链表是否为空：', sll.is_empty())
print('当前链表长度：', sll.length())
print('遍历链表：', end='')
sll.travel()
print('\n------在指定位置插入节点-----')
sll.insert(0, 8)
sll.insert(2, 9)
sll.insert(9, 10)
sll.insert(10, 10)
print('当前链表是否为空：', sll.is_empty())
print('当前链表长度：', sll.length())
print('遍历链表：', end='')
sll.travel()
print('\n------删除指定位置的元素，实现的效果类似列表的remove方法-----')
sll.remove(7)
sll.remove(1)
sll.remove(10)
print('当前链表是否为空：', sll.is_empty())
print('当前链表长度：', sll.length())
print('遍历链表：', end='')
sll.travel()
"""
当前链表是否为空： True
当前链表长度： 0
------在链表尾部添加节点------
当前链表是否为空： False
当前链表长度： 1
当前链表是否为空： False
当前链表长度： 6
遍历链表：1 2 3 4 5 6 
------在链表头部添加节点-----
当前链表是否为空： False
当前链表长度： 7
遍历链表：7 1 2 3 4 5 6 
------在指定位置插入节点-----
当前链表是否为空： False
当前链表长度： 11
遍历链表：8 7 9 1 2 3 4 5 6 10 10 
------删除指定位置的元素，实现的效果类似列表的remove方法-----
当前链表是否为空： False
当前链表长度： 8
遍历链表：8 9 2 3 4 5 6 10
"""
