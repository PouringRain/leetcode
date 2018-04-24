# level : medium

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if s=='': return 0

        start, m, ans = 0, 0, 0
        sub = []
        for i, c in enumerate(s):
            if c not in sub:
                sub.append(c)
                m += 1
            else:
                ans = max(m, ans)
                lenth = len(sub)
                start = sub.index(c) + 1
                sub = sub[start:] + [c]
                m = len(sub)
                # print m

        return max(ans, m)