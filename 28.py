# level: eazy

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if needle in haystack:
            if haystack == '':
                return 0
            if needle == '':
                return 0
            return haystack.index(needle)
        else:
            return -1