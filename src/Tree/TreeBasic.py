__author__ = 'mingchen'

from random import randint

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def addLeft(self, left):
        self.left = left

    def addRight(self, right):
        self.right = right

    def preOrderTraverse(self):
        print self.val

        self.doTraverse(self.left, "preOrderTraverse")
        self.doTraverse(self.right, "preOrderTraverse")

    def inOrderTraverse(self):
        self.doTraverse(self.left, "inOrderTraverse")
        print self.val
        self.doTraverse(self.right, "inOrderTraverse")

    def postOrderTraverse(self):
        self.doTraverse(self.right, "postOrderTraverse")
        print self.val
        self.doTraverse(self.left, "postOrderTraverse")

    def doTraverse(self, node, traverse):
        if node is None:
            print None
        else:
            method = getattr(node, traverse)
            if not method:
                raise Exception("Traverse method %s not implemented" % method)
            else:
                method()

def constructCompleteBinaryTree(height):
    if height is 0:
        return None
    elif height is 1:
        return TreeNode(randint(0, 100))
    else:
        root = TreeNode(randint(0, 100))
        root.addLeft(constructCompleteBinaryTree(height - 1))
        root.addRight(constructCompleteBinaryTree(height - 1))
        return root

if __name__ == "__main__":
    root = TreeNode(5)
    root.addLeft(TreeNode(10))
    root.inOrderTraverse()

