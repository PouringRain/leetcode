# level: medium

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sorted(nums)
        res = [[]]

        for num in nums:
            res += [i + [num] for i in res]
        return res