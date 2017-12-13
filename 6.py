class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        epoch = numRows * 2 - 2
        result = []
        for i in range(numRows):
            result.append([])
        # nodes = [['' for i in range(100)] for i in range(numRows)]
        for i in range(len(s)):
            t = int(i % epoch)

            if t < numRows:
                result[t].append(s[i])
            else:
                result[epoch - t].append(s[i])
        mystr = ''
        for i in range(numRows):
            mystr += ''.join(result[i])

        return mystr

if __name__ == '__main__':
    ans = Solution()
    print(ans.convert('PAYPALISHIRING', 4))
