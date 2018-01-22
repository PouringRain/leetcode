# level: medium
# solution: greedy algorithm

class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans = 0
        nowMax = -1

        for i, v in enumerate(arr):
            nowMax = max(nowMax, v)
            if nowMax == i:
                ans += 1

        return ans

if __name__ == '__main__':
    ans = Solution()
    print(ans.maxChunksToSorted([1,0,2,3,4]))