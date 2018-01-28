class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        if J == '' or S == '':
            return 0

        ans = 0
        for j in J:
            ans += S.count(j)

        return ans