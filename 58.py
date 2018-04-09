# level: eazy

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s.strip()=='': return 0
        last = s.split()[-1]
        return len(last)