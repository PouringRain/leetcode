# level: medium

class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        for i in range(len(A)):
            if abs(i - A[i]) > 1:
                return False

        return True

