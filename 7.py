# level: eazy

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        # -2^31 ~ 2^31-1

        if x < 0:
            x = 0 - int(str(abs(x))[::-1])
            if x < 0 - 2 ** 31 or x > 2 ** 31 - 1:
                return 0
            else:
                return x
        else:
            x = int(str(x)[::-1])
            if x < 0 - 2 ** 31 or x > 2 ** 31 - 1:
                return 0
            else:
                return x
if __name__ == '__main__':
    ans = Solution()
    print(ans.reverse(-123))
