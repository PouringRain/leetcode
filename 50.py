# level: medium

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0: return 1.0
        pos = 1 if n>0 else 0
        n = abs(n)
        ret = 1
        cur = x
        while n:
            if n&1==1:
                ret *= cur
            cur *= cur
            n>>=1
        return ret if pos else 1/ret
