# level: eazy

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '': return -1

        count = {}

        for i, w in enumerate(s):
            if count.has_key(w):
                count[w] += 1
            else:
                count[w] = 1
        # print count
        for i, w in enumerate(s):
            if count[w] == 1:
                return i

        return -1
if __name__ == '__main__':
    ans = Solution()
    print(ans.firstUniqChar('leetcode'))