# level: eazy
import collections
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = collections.Counter(s)
        for c in t:
            if d[c]:
                d[c]-=1
            else:
                return c