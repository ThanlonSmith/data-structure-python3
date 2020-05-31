class Queue():
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        # 如果出队比入队操作频率高
        # self.__list.insert(0, item)
        # 如果入队比出队操作频率高
        self.__list.append(item)

    def dequeue(self):
        # 如果出队比入队操作频率高
        # self.__list.pop()
        # 如果入队比出队操作频率高
        return self.__list.pop(0)

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)


# 创建一个空的双端队列
q = Queue()
q.enqueue(1)
q.enqueue(1.2)
q.enqueue('thanlon')
q.enqueue([1, 2, 3])
print('入队状态：已完成')
print('当前队列是否为空：', q.is_empty())
print('当前队列的大小：', q.size())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
"""
入队状态：已完成
当前队列是否为空： False
当前队列的大小： 4
1
1.2
thanlon
[1, 2, 3]
"""