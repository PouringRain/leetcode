# level: eazy
# solution: rob[i] = max(rob[i - 1], rob[i - 2] + nums[i])

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []: return 0
        if len(nums) <= 2: return max(nums)
        rob = [0] * len(nums)

        rob[0] = nums[0];
        rob[1] = max(nums[0], nums[1]);

        for i in range(2, len(nums)):
            rob[i] = max(rob[i - 1], rob[i - 2] + nums[i])

        return rob[-1]