# level: eazy

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = min(nums)
        step = 0
        for num in nums:
            step+=num-m
        return step
if __name__=='__main__':
    ans = Solution()
    print(ans.minMoves([1,2,3]))