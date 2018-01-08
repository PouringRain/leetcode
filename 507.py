class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1: return False
        total = 1
        i = 2
        while i * i < num:
            if num % i == 0:
                total += i + num / i
            i += 1

        if total == num:
            return True
        else:
            return False

if __name__=='__main__':
    ans = Solution()
    print(ans.checkPerfectNumber(28))