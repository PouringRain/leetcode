class Solution:
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        pos, i = 0, 0
        while 1:
            i += 1
            pos += i
            if pos >= target and (pos-target)%2 == 0:
                break

        return i

if __name__ == '__main__':
    ans = Solution()
    print(ans.reachNumber(2))