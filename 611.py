# level: medium
# 思路：双向指针

class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = sorted(nums)
        result = 0
        for i in range(len(nums) - 1, 1, -1):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i] and nums[left] != 0:
                    result += right - left
                    right -= 1
                else:
                    left += 1

        return result
