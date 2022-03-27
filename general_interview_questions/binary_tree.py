
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def getVal(self):
        return self.val

    def __str__(self):
        return f'value is {self.val}'

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.val:
            if node.left is not None:
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right is not None:
                self._add(val, node.right)
            else:
                node.right = Node(val)

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.val:
            return node
        elif (val < node.val and node.left is not None):
            return self._find(val, node.left)
        elif (val > node.val and node.right is not None):
            return self._find(val, node.right)

    def deleteTree(self):
        self.root = None

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.left)
            print(f'{node.val}')
            self._printTree(node.right)

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)
        else:
            print('empty tree')

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))


tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()
depth = tree.maxDepth(tree.getRoot())
print(f'maxDepth is {depth}')

x = tree.find(3)
print(f'{x}')
x = tree.find(100)
if x is None:
    print('x was not found in the tree, expected result')
