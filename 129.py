# level: medium

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root: return 0
        self.res = 0

        def dfs(root, ans, res):
            if not root.left and not root.right:
                self.res += ans * 10 + root.val
                return
            if root.left:
                dfs(root.left, ans * 10 + root.val, res)
            if root.right:
                dfs(root.right, ans * 10 + root.val, res)

        dfs(root, 0, self.res)
        return self.res