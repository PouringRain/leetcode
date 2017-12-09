# coding=utf-8


# difficult: Medium
# 思路：翻转该数，将递增位置之前全赋值为9，下一位减1

class Solution:
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        # convert number to strlist
        n = list(str(N)[::-1])
        l = len(n)
        for i in range(l-1):
            if n[i] < n[i+1]:
                n[:i+1] = '9'*(i+1)
                n[i+1] = str(int(n[i+1])-1)

        return int(''.join(reversed(n)))


if __name__ == '__main__':
    ans = Solution()
    print(ans.monotoneIncreasingDigits(332))
