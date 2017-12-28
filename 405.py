# level:eazy
# 注意负数的处理

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num == 0: return '0'
        result = []
        # 遇到负数
        if num < 0:
            num += 0x100000000

        hex = '0123456789abcdef'
        while num > 0:
            a = num % 16
            num = num / 16
            result.insert(0, hex[a])

        return ''.join(result)

if __name__ == '__main__':
    ans = Solution()
    print(ans.toHex(26))
    print(ans.toHex(-1))