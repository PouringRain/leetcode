# level: eazy

class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """

        maxlen = (len(B) + len(A)) * 3
        ans, sub = 1, A

        while len(sub) < maxlen:
            if B in sub:
                return ans
            else:
                sub += A
                ans += 1

        return -1
