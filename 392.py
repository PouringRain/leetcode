# level : medium
# solution: dp会超时，所以改为two pointer来做

# class Solution(object):
#     def isSubsequence(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         x, y = len(s), len(t)
#         dp = [ [0]* (y+1) for _ in range(x+1)]
#         # print dp
#         for i in range(1, x+1):
#             for j in range(1, y+1):
#                 if s[i-1]==t[j-1]:
#                     dp[i][j] = dp[i-1][j-1]+1
#                 else:
#                     dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#                 if dp[i][j]==x:
#                     return True

#         if dp[-1][-1]==x:
#             return True
#         else:
#             return False

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == '': return True

        p, q = -1, -1
        for _ in range(len(t)):
            if s[p + 1] == t[q + 1]:
                p += 1
                q += 1
            else:
                q += 1
            if p == len(s) - 1: return True
        return False
