__author__ = 'mingchen'
from TreeBasic import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root is not None:
            tmp = root.left
            root.left = root.right
            root.right = tmp
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

if __name__ == '__main__':
    root = TreeNode(5)
    root.addLeft(TreeNode(1))
    root.addRight(TreeNode(9))
    root.inOrderTraverse()

    print " after invert"

    s = Solution()
    root = s.invertTree(root)
    root.inOrderTraverse()


