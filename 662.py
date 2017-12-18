# level:medium
# 思路：广度遍历，计算二叉树每层最大宽度，取最大值

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from Queue import Queue


class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxdis = 1
        q = Queue()
        # if root.left == root.right == None: return 1
        root.val = 1
        q.put(root)

        while not q.empty():
            left, right = float("inf"), float("-inf")
            n = q.qsize()
            for i in range(n):
                node = q.get()
                if node.left != None:
                    node.left.val = node.val * 2 - 1
                    if node.left.val > right:
                        right = node.left.val
                    if node.left.val < left:
                        left = node.left.val

                    q.put(node.left)
                if node.right != None:
                    node.right.val = node.val * 2
                    if node.right.val < left:
                        left = node.right.val
                    if node.right.val > right:
                        right = node.right.val

                    q.put(node.right)


            maxdis = max(maxdis, right - left + 1)

        return maxdis

if __name__ == '__main__':
    ans = Solution()
    print(ans.widthOfBinaryTree([1,3,2,5,3,None,9]))
