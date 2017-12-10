# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #ans = 0
        if not root:
            return 0
        left, right, val = root.left, root.right, root.val
        return max(self.longest_val(left, val) + self.longest_val(right, val), \
                    self.longestUnivaluePath(left),\
                       self.longestUnivaluePath(right)
                       )


    def longest_val(self, root, val):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root or root.val != val:
            return 0
        else:
            return 1 + max(self.longest_val(root.left, val) , self.longest_val(root.right, val))

if __name__ == '__main__':
    ans = Solution()
    print(ans.longestUnivaluePath([5,4,5,1,1,5]))
