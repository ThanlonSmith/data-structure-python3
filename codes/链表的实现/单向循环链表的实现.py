class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class CircularlinkedList:
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        """
        判断是否为空
        :return:
        """
        return self.__head == None

    def lencllth(self):
        """
        获取链表的长度
        :return:
        """
        # 如果是空链表
        if self.is_empty():
            return 0
        # 只有一个节点，也是可以处理的
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """
        遍历所有节点中的元素
        :return:
        """
        # 如果是空链表则不作任何操作
        if self.is_empty():
            return
        # 如果只有一个节点也是可以处理的
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=' ')
            cur = cur.next
        print(cur.elem)

    def add(self, elem):
        """
        头部插入
        :param elem:
        :return:
        """
        node = Node(elem)
        # 如果是空链表
        if self.is_empty():
            self.__head = node
            node.next = node
            return
        # 只有一个节点，也是可以处理的
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
        node.next = self.__head
        self.__head = node
        # cur.next = node
        cur.next = self.__head

    def append(self, elem):
        """
        尾部插入
        :param elem:
        :return:
        """
        node = Node(elem)
        # 链表为空
        if self.is_empty():
            self.__head = node
            node.next = node
            return
        # 也适用于链表只有一个节点
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
        # node.next = cur.next
        node.next = self.__head
        cur.next = node

    def insert(self, pos, elem):
        if pos <= 0:
            self.add(elem)
        elif pos > self.lencllth() - 1:
            self.append(elem)
        else:
            # 因为不涉及头节点和尾节点的链接，中间插入和单链表插入方式一样
            count = 0
            pre = self.__head
            while count < pos - 1:
                count += 1
                pre = pre.next
            # 循环退出之后，pre指向post-1的位置
            node = Node(elem)
            node.next = pre.next
            pre.next = node

    def search(self, elem):
        if self.is_empty():
            return False
        cur = self.__head
        while cur != self.__head:
            if cur.elem == elem:
                return True
            cur = cur.next
        if cur.elem == elem:
            return True
        return False

    def remove(self, elem):
        if self.is_empty():
            return
        cur = self.__head
        prev = None
        while cur.next != self.__head:
            if cur.elem == elem:
                # 判断是否是头节点
                if cur == self.__head:
                    rear = self.__head
                    # 通过循环找到尾节点
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    # 删除中间节点
                    prev.next = cur.next
                return
            prev = cur
            cur = cur.next
        # 上述循环之后，最后一个节点的元素没有判断，所以需要判断
        if cur.elem == elem:
            # 如果链表只有一个节点
            if cur.next == self.__head:
                self.__head = None
            # prev.next = cur.next
            prev.next = self.__head


cll = CircularlinkedList()
print('------链表初始化信息-----')
print('当前链表是否为空：', cll.is_empty())
print('当前链表长度：', cll.lencllth())
print('------在链表尾部添加节点------')
cll.append(1)
cll.append(2)
cll.append(3)
cll.append(4)
cll.append(5)
cll.append(6)
print('当前链表是否为空：', cll.is_empty())
print('当前链表长度：', cll.lencllth())
print('遍历链表：', end='')
cll.travel()
print('\n------在链表头部添加节点-----')
cll.add(7)
print('当前链表是否为空：', cll.is_empty())
print('当前链表长度：', cll.lencllth())
print('遍历链表：', end='')
cll.travel()
print('\n------在指定位置插入节点-----')
cll.insert(0, 8)
cll.insert(2, 9)
cll.insert(9, 10)
cll.insert(10, 10)
print('当前链表是否为空：', cll.is_empty())
print('当前链表长度：', cll.lencllth())
print('遍历链表：', end='')
cll.travel()
print('\n------删除指定位置的元素，实现的效果类似列表的remove方法-----')
cll.remove(8)
cll.remove(1)
cll.remove(10)
print('当前链表是否为空：', cll.is_empty())
print('当前链表长度：', cll.lencllth())
print('遍历链表：', end='')
cll.travel()
"""
------链表初始化信息-----
当前链表是否为空： True
当前链表长度： 0
------在链表尾部添加节点------
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
遍历链表：7 9 2 3 4 5 6 10
"""