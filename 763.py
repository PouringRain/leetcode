# level: medium
# 思路：双指针+递归

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = []

        def get_sub(s):
            if not s:
                return
            l, r = 0, len(s) - s[::-1].index(s[0]) - 1
            while l < r:
                l += 1
                if len(s) - s[::-1].index(s[l]) - 1 > r:
                    r = len(s) - s[::-1].index(s[l]) - 1
            res.append(l + 1)
            get_sub(s[l + 1:])

        get_sub(S)
        return res

if __name__ == '__main__':
    ans = Solution()
    print(ans.partitionLabels("ababcbacadefegdehijhklij"))