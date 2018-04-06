# level: medium
# solution：前序遍历根节点在开始的位置，中序遍历根的左边是左子树，根的右边是右子树

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # preorder = [3,9,20,15,7]
        # inorder = [9,3,15,20,7]
        if not inorder:
            return None

        rootIndex = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[rootIndex])
        root.left = self.buildTree(preorder, inorder[:rootIndex])
        root.right = self.buildTree(preorder, inorder[rootIndex + 1:])

        return root