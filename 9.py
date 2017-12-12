class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        low, high = -2 ** 31, 2 ** 31 - 1
        i, j = 0, len(str(x)) - 1
        x = str(x)
        while i < j:
            if x[i] == x[j]:
                i += 1
                j -= 1
            else:
                return False
        if int(x) < low or int(x) > high:
            return 0
        else:
            return True
if __name__ == '__main__':
    ans = Solution()
    print(ans.isPalindrome(-123))