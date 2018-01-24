# level: medium

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []: return []
        row = len(matrix)
        col = len(matrix[0])
        res = []
        # if row == 1 or col == 1:
        #     for i in range(row):
        #         for j in range(col):
        #             res.append(matrix[i][j])
        #     return res

        sx, ex, sy, ey = 0, row - 1, 0, col - 1
        while sx <= ex and sy <= ey:
            for i in range(sy, ey + 1):
                res.append(matrix[sx][i])
            sx += 1
            for i in range(sx, ex + 1):
                res.append(matrix[i][ey])
            ey -= 1
            for i in range(ey, sy - 1, -1):
                res.append(matrix[ex][i])
            ex -= 1
            for i in range(ex, sx - 1, -1):
                res.append(matrix[i][sy])
            sy += 1

        return res[:row * col]

if __name__ == '__main__':
    ans = Solution()
    print(ans.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
    print(ans.spiralOrder([[2,5], [8,4], [0,-1]]))
    print(ans.spiralOrder([[2], [8], [0]]))
