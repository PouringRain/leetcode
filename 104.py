# level: medium
# solution: 递归

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root):
            if not root:
                return 0

            return max(dfs(root.left) + 1 if root.left else 1, \
                       dfs(root.right) + 1 if root.right else 1)

        ans = dfs(root)
        return ans