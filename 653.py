# level: eazy

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        nums = []

        def inorder_travel(node):
            if not node: return
            if node.left:
                inorder_travel(node.left)
            nums.append(node.val)
            if node.right:
                inorder_travel(node.right)

        inorder_travel(root)

        i, j = 0, len(nums) - 1
        while i < j:
            t = nums[i] + nums[j]
            if t == k:
                return True
            elif t < k:
                i += 1
            else:
                j -= 1
        return False