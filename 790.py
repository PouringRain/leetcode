class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1: return 1

        a, b, c = 1, 1, 2
        for i in range(3, N + 1):
            t = b
            b = c
            c = c * 2 + a
            a = t

        return c % (10 ** 9 + 7)