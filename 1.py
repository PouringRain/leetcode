class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # hashset
        dic = {}
        for i, num in enumerate(nums):
            if dic.has_key(target-num):
                return [dic[target-num], i]
            else:
                dic[num]=i
        return []
