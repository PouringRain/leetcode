# level: medium

class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        age = collections.Counter(ages)
        ans = 0
        for A in age:
            for B in age:
                if B==A:
                    if B <= 0.5 * A + 7 or B > A or (B > 100 and A < 100):
                        continue
                    # 不能和自己交朋友
                    ans+=age[A]*(age[A]-1)
                else:
                    if B <= 0.5 * A + 7 or B > A or (B > 100 and A < 100):
                        continue
                    ans+=age[A]*age[B]
        return ans