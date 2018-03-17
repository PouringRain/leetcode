# solution: 并查集

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        m = -1
        for x, y in edges:
            if m < max(x, y):
                m = max(x, y)
                
        pre = [i for i in range(m + 1)]

        def find(r):
            while pre[r] != r:
                r = pre[r]
            return r

        for x, y in edges:
            fx, fy = find(x), find(y)
            if fx == fy:
                return [x, y]
            else:
                pre[fx] = y
