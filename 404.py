# Definition for a binary tree node.

# level : eazy

class Solution(object):


    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.bfs(root, False)

    def bfs(self, root, isleft):
        """
        :type root: TreeNode
        :type isleft: bool
        """
        if root == None: return 0
        if root.left == None and root.right == None and isleft:
            return root.val
        else:
            return self.bfs(root.left, True) + self.bfs(root.right, False)

