# level: hard
# solution: greedy algorithm

class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(0, len(row) - 1, 2):
            if row[i] % 2 == 0:
                if row[i + 1] == row[i] + 1:
                    pass
                else:
                    index = row.index(row[i] + 1)
                    row[i + 1], row[index] = row[index], row[i + 1]
                    ans += 1
            else:
                if row[i + 1] == row[i] - 1:
                    pass
                else:
                    index = row.index(row[i] - 1)
                    row[i + 1], row[index] = row[index], row[i + 1]
                    ans += 1

        return ans

if __name__ == '__main__':
    ans = Solution()
    print(ans.minSwapsCouples([0, 2, 1, 3]))