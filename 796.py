# level: eazy

class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        for i in range(len(A) - 1):
            if A[i + 1:] + A[:i + 1] == B:
                return True

        return False
