# coding='utf-8'
# level: medium
# 思路：可以用dp来解，下面的方法不是。以单个数字或两个数字为中心向两边扩展
class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        len_s = len(s)
        for i in range(len_s):
            result += 1
            start, end = i - 1, i + 1
            while start >= 0 and end < len_s:
                if s[start] == s[end]:
                    result += 1
                    start -= 1
                    end += 1
                else:
                    break
            start, end = i - 1, i
            while start >= 0 and end < len_s:
                if s[start] == s[end]:
                    result += 1
                    start -= 1
                    end += 1
                else:
                    break
        return result


if __name__ == '__main__':
    ans = Solution()
    print(ans.countSubstrings("aaa"))
