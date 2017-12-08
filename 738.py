# coding=utf-8


# Input: N = 1234
# Output: 1234

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