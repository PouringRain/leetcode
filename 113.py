# level: medium

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []

        def helper(root, s, temp):
            if not root: return
            # leaf
            # print temp
            if not root.left and not root.right and root.val == s:
                # print temp
                res.append(temp + [root.val])
                return
                # not leaf
            if root.left:
                helper(root.left, s - root.val, temp + [root.val])
            if root.right:
                helper(root.right, s - root.val, temp + [root.val])

        helper(root, sum, [])
        return res
