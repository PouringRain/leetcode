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
    
 class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return []
        ret = []
        curset = []

        def dfs(start, curset, nums, ret):
            # print(curset)
            ret.append(copy.deepcopy(curset))
            # print(res)
            for i in range(start, len(nums)):
                curset.append(nums[i])
                dfs(i+1, curset, nums, ret)
                curset.pop()

        dfs(0, [], nums, ret)

        return ret
