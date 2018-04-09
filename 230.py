# level: medium

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        nums = []

        def inorderSearchK(root):
            if not root: return
            if root.left:
                inorderSearchK(root.left)
            nums.append(root.val)
            self.k -= 1
            if self.k == 0: return
            if root.right:
                inorderSearchK(root.right)

        inorderSearchK(root)

        return nums[k - 1]