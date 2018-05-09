# level: medium
# solution: dp. f(i,n) = g(i-1)*g(n-i)

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        g = [0] * (n + 1)
        g[0] = g[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                g[i] += g[j - 1] * g[i - j]

        return g[n]