class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []

        lenth = len(M[0])
        height = len(M)

        for i in range(height):
            i_result = []
            for j in range(lenth):
                sum = 0
                n = 0
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if not (x < 0 or x > height - 1 or y < 0 or y > lenth - 1):
                            sum += M[x][y]
                            n += 1
                i_result.append(sum // n)
            result.append(i_result)

        return result

if __name__ == '__main__':
    ans = Solution()
    print(ans.imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))