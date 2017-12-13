# level: medium
# 思路：dfs 将节点设为子树和，统计出现最多的字数和

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict

class Solution(object):
    nodes = defaultdict(int)

    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.nodes.clear()
        self.dfs(root)
        result = []
        vals = []
        m = -9999
        # print(self.nodes)
        for key, val in self.nodes.items():
            if val > m: m = val
        for key, val in self.nodes.items():
            if val == m:
                result.append(key)
        return result

    def dfs(self, root):
        if root == None:
            return

        if root.left != None:
            self.dfs(root.left)
            root.val += root.left.val

        if root.right != None:
            self.dfs(root.right)
            root.val += root.right.val

        self.nodes[root.val] += 1


if __name__ == '__main__':
    ans = Solution()
    print(ans.findFrequentTreeSum([5, 2, -3]))
