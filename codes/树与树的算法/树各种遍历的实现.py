class Node:
    def __init__(self, elem, l_child=None, r_child=None):
        self.elem = elem  # 节点本身的值
        self.l_child = l_child  # 左孩子
        self.r_child = r_child  # 右孩子


class Tree:
    def __init__(self, root=None):
        self.root = root

    def add_node(self, elem):
        # 创建一个节点
        node = Node(elem)
        # 如果根节点为空，则为根节点赋值
        if self.root == None:
            self.root = node
        # 否则继续判断
        else:
            # 创建一个队列并加入根节点
            queue = [self.root]
            while queue:
                # 弹出第一个节点
                curr_node = queue.pop(0)
                # 如果该节点的左孩子为空，则需要创建的节点赋给当前节点的左孩子节点
                if curr_node.l_child is None:
                    curr_node.l_child = node
                    return
                # 如果该节点的右孩子为空，则需要创建的节点赋给当前节点的右孩子节点
                elif curr_node.r_child is None:
                    curr_node.r_child = node
                    return
                # 如果该节点的左孩子和右孩子都有值，则需要将左右孩子加入队列继续判断它们有没有孩子节点
                else:
                    queue.append(curr_node.l_child)
                    queue.append(curr_node.r_child)

    def breadth_traversal(self):
        """广度优先遍历/层次遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            curr_node = queue.pop(0)
            print(curr_node.elem, end=' ')
            if curr_node.l_child is not None:
                queue.append(curr_node.l_child)
            if curr_node.r_child is not None:
                queue.append(curr_node.r_child)

    def preorder_traversal(self, root):
        """递归实现先序遍历"""
        if root is None:
            return
        print(root.elem, end=' ')
        self.preorder_traversal(root.l_child)
        self.preorder_traversal(root.r_child)

    def inorder_traversal(self, root):
        """递归实现中序遍历"""
        if root is None:
            return
        self.inorder_traversal(root.l_child)
        print(root.elem, end=' ')
        self.inorder_traversal(root.r_child)

    def postorder_traversal(self, root):
        """递归实现后续遍历"""
        if root is None:
            return
        self.postorder_traversal(root.l_child)
        self.postorder_traversal(root.r_child)
        print(root.elem, end=' ')


tree = Tree()
# 第一个赋值给根节点
tree.add_node(0)
# 为根节点的左孩子赋值
tree.add_node(1)
# 为根节点的右孩子赋值
tree.add_node(2)
# 为根节点的左孩子的左孩子赋值
tree.add_node(3)
# 为根节点的左孩子的右孩子赋值
tree.add_node(4)
# 为根节点的右孩子的左孩子赋值
tree.add_node(5)
# 为根节点的右孩子的右孩子赋值
tree.add_node(6)
tree.add_node(7)
tree.add_node(8)
tree.add_node(9)
print('广度优先遍历(层次遍历)：', end='')
tree.breadth_traversal()
print('\n前序遍历：', end='')
tree.preorder_traversal(tree.root)
print('\n中序遍历：', end='')
tree.inorder_traversal(tree.root)
print('\n后序遍历：', end='')
tree.postorder_traversal(tree.root)
"""
广度优先遍历(层次遍历)：0 1 2 3 4 5 6 7 8 9 
前序遍历：0 1 3 7 8 4 9 2 5 6 
中序遍历：7 3 8 1 9 4 0 5 2 6 
后序遍历：7 8 3 9 4 1 5 6 2 0 
"""
