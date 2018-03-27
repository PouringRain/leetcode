class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # new = copy.deepcopy(grid)
        # print new

        ans = 0
        row, col = len(grid), len(grid[0])
        bottom = [0] * col
        left = [0] * row

        # cal the direct of bottom
        for i in range(col):
            nums = []
            for j in range(row):
                nums.append(grid[j][i])
            bottom[i] = max(nums)
        # print bottom


        # cal the direct of left
        for i in range(row):
            left[i] = max(grid[i])
        # print left

        for i in range(row):
            for j in range(col):
                ans += min(bottom[j], left[i]) - grid[i][j]

        return ans