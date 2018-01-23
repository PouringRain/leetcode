class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for i in range(int(c ** 0.5 + 1)):
            j = c - i ** 2
            if (int(j ** 0.5) ** 2) == j:
                return True

        return False
    

if __name__ == '__main__':
    ans = Solution()
    print(ans.judgeSquareSum(5))
