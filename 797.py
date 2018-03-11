# level: medium
# solution: 递归，典型的递归！！！

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(graph)

        def dfs(node):
            if node == n - 1:
                return [[n - 1]]

            res = []
            for i in graph[node]:
                for path in dfs(i):
                    res.append([node] + path)
            return res

        return dfs(0)
