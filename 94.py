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
    
    # 非递归实现
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        cur, res = root, []
        while cur!=None or stack:
            while cur!=None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        
        return res
