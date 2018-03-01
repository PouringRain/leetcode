# level: medium

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(str(num))

        for i in range(len(num) - 1):
            m = max(num[i + 1:])
            for j in range(len(num) - 1, i - 1, -1):
                if num[i] < num[j] and num[j] == m:
                    num[i], num[j] = num[j], num[i]
                    return int(''.join(num))

        return int(''.join(num))