# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getDepth(self, root, depth=0):
        if not root: return depth
        if not root.left and not root.right:
            return depth + 1
        return 1 + max(self.getDepth(root.left), self.getDepth(root.right))

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        left = self.getDepth(root.left)
        right = self.getDepth(root.right)

        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)