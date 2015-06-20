__author__ = 'mingchen'
# Definition for a binary tree node.
# class TreeNode:
# def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from TreeBasic import TreeNode, constructCompleteBinaryTree


class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if root is None:
            return 0
        else:
            leftHeight = self.getHeight(root, "left")
            if leftHeight == self.getHeight(root, "right"):
                return 2 ** leftHeight - 1
            else:
                return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def getHeight(self, node, child):
        if child not in ["left", "right"]:
            raise Exception("Incorrect child input: %s" % child)

        if node is None:
            return 0
        else:
            return 1 + self.getHeight(getattr(node, child), child)

    # def countNodes(self, root):
    #     if not root:
    #         return 0
    #     else:
    #         lHeight = rHeight = 1
    #         left = root.left
    #         while left:
    #             lHeight += 1
    #             left = left.left
    #         right = root.right
    #         while right:
    #             rHeight += 1
    #             right = right.right
    #
    #         if lHeight == rHeight:
    #             return 2**lHeight - 1
    #         else:
    #             return 1 + self.countNodes(left) + self.countNodes(right)

if __name__ == "__main__":
    root = TreeNode(0)
    root.addLeft(TreeNode(0))
    root.addRight(TreeNode(0))

    s = Solution()
    print s.countNodes(constructCompleteBinaryTree(0))
    print s.countNodes(constructCompleteBinaryTree(2))
    print s.countNodes(constructCompleteBinaryTree(5))
    print s.countNodes(constructCompleteBinaryTree(9))

