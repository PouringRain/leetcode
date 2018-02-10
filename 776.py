# level: medium

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        if root==None: return [None, None]
        if root.val==V:
            p = root.right
            root.right = None
            return [root, p]
        if root.val>V:
            small, large = self.splitBST(root.left, V)
            root.left = large
            return [small, root]
        if root.val<V:
            small, large = self.splitBST(root.right, V)
            root.right = small
            return [root, large]