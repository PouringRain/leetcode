# level: eazy

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        row = len(matrix)
        col = len(matrix[0])

        i = 0
        for j in range(col - 1):
            nowj = j
            while i + 1 < row and nowj + 1 < col:
                if matrix[i][nowj] != matrix[i + 1][nowj + 1]:
                    return False
                i += 1
                nowj += 1

        j = 0
        for i in range(row - 1):
            nowi = i
            while j + 1 < col and nowi + 1 < row:
                if matrix[nowi][j] != matrix[nowi + 1][j + 1]:
                    return False
                j += 1
                nowi += 1

        return True

if __name__ == '__main__':
    ans = Solution()
    print(ans.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))