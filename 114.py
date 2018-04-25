# level: medium
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    prev = None
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root: return
        self.prev = root
        self.flatten(root.left)
        tmp = root.right
        root.left, root.right = None, root.left
        self.prev.right = tmp
        self.flatten(root.right)