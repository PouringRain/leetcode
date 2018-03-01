# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        res = []

        def traversal(node):
            if not node:
                return None
            elif node.val < L:
                return traversal(node.right)
            elif node.val > R:
                return traversal(node.left)
            else:
                node.left = traversal(node.left)
                node.right = traversal(node.right)
                return node

        return traversal(root)