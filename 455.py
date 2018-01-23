# level: eazy
# greedy algorithm

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g, s = sorted(g), sorted(s)

        ans = 0
        for c in g:
            if s:
                for i, cookie in enumerate(s):
                    if cookie >= c:
                        ans += 1
                        del s[i]
                        break

        return ans

if __name__ == '__main__':
    ans = Solution()
    print(ans.findContentChildren([1,2],[1,2,3]))