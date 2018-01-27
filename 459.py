# level: eazy

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        bl = l // 2
        sl = list(s)
        # print l, bl, sl
        for i in range(bl):
            if l % (i + 1) == 0:
                sub = sl[:i + 1]
                t = l / (i + 1)
                # print t
                total = sub * t
                # print total
                if ''.join(total) == s:
                    return True

        return False

if __name__ == '__main__':
    ans = Solution()
    print(ans.repeatedSubstringPattern('abab'))