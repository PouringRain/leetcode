# level: eazy
# solution: 递归

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def isPalindrome(s, l, r, flag):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    if flag == 1:
                        return False
                    else:
                        return isPalindrome(s, l + 1, r, 1) or isPalindrome(s, l, r - 1, 1)
            return True

        return isPalindrome(s, 0, len(s) - 1, 0)