# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return -1
        self.ans, minVal = float("inf"), root.val

        def dfs(node):
            if node:
                if minVal < node.val < self.ans:
                    self.ans = node.val
                    return
                elif node.val == minVal:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        if self.ans == float("inf"):
            return -1
        else:
            return self.ans