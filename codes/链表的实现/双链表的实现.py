class DoubleNode:
    def __init__(self, elem):
        self.elem = elem
        self.prev = None
        self.next = None


class DoubleLinkedList():
    def __init__(self):
        self.__head = None

    def is_empty(self) -> bool:
        """
        判断是否为空
        :return:
        """
        return self.__head is None

    def length(self) -> int:
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

    def add(self, item):
        """
        头插法
        :param item:
        :return:
        """
        node = DoubleNode(item)
        if self.is_empty():
            self.__head = node
            return
        node.next = self.__head
        self.__head = node
        node.next.prev = node

    def append(self, elem):
        """
        尾部添加元素
        :param elem:
        :return:
        """
        node = DoubleNode(elem)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, elem):
        node = DoubleNode(elem)
        if pos <= 0:
            self.add(elem)
        elif pos > self.length() - 1:
            self.append(elem)
        else:
            cur = self.__head
            count = 0
            while count < pos:
                cur = cur.next
                count += 1
            # 第一种方式
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node
            # 第二种方式
            """
            cur.prev = node
            node.prev.next = node
            """

    def search(self, elem) -> bool:
        cur = self.__head
        while cur is not None:
            if cur.elem == elem:
                return True
            else:
                cur = cur.next
        return False

    def remove(self, elem):
        cur = self.__head
        while cur is not None:
            if cur.elem == elem:
                if cur == self.__head:
                    self.__head = cur.next
                    # 判断链表是否只有一个节点
                    if cur.next:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next


dll = DoubleLinkedList()
print('-------初始的链表------')
print('当前链表是否为空：', dll.is_empty())
print('当前链表的长度：', dll.length())
print('------头插法添加链表------')
dll.add(1)
dll.add(2)
dll.add(3)
print('当前链表是否为空：', dll.is_empty())
print('当前链表的长度：', dll.length())
print('遍历链表：', end='')
dll.travel()
print('\n------尾插法添加链表------')
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
print('当前链表是否为空：', dll.is_empty())
print('当前链表的长度：', dll.length())
print('遍历链表：', end='')
dll.travel()
print('\n------指定位置插入------')
dll.insert(0, 6)
dll.insert(2, 7)
dll.insert(5, 8)
print('当前链表是否为空：', dll.is_empty())
print('当前链表的长度：', dll.length())
print('遍历链表：', end='')
dll.travel()
print('\n------查找元素------')
print('当前链表是否为空：', dll.is_empty())
print('当前链表的长度：', dll.length())
print('遍历链表：', end='')
dll.travel()
print('\n链表中是否存在元素是2的节点：%s' % dll.search(2))
print('------删除元素(这里以删除头节点6为例子)------')
dll.remove(6)
print('当前链表是否为空：', dll.is_empty())
print('当前链表的长度：', dll.length())
print('遍历链表：', end='')
dll.travel()
"""
-------初始的链表------
当前链表是否为空： True
当前链表的长度： 0
------头插法添加链表------
当前链表是否为空： False
当前链表的长度： 3
遍历链表：3 2 1 
------尾插法添加链表------
当前链表是否为空： False
当前链表的长度： 7
遍历链表：3 2 1 1 2 3 4 
------指定位置插入------
当前链表是否为空： False
当前链表的长度： 10
遍历链表：6 3 7 2 1 8 1 2 3 4 
------查找元素------
当前链表是否为空： False
当前链表的长度： 10
遍历链表：6 3 7 2 1 8 1 2 3 4 
链表中是否右元素是2的节点：True
------删除元素------
当前链表是否为空： False
当前链表的长度： 9
遍历链表：3 7 2 1 8 1 2 3 4 
"""
