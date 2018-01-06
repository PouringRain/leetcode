class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        a, b = m, n
        for item in ops:
            if a > item[0]:
                a = item[0]
            if b > item[1]:
                b = item[1]

        return a * b
