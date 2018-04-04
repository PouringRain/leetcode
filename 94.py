# level: medium

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        def travel(root):
            if not root: return
            if root.left:
                travel(root.left)
            res.append(root.val)
            if root.right:
                travel(root.right)

        travel(root)
        return res