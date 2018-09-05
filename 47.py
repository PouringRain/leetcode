# level: medium

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        def backtrack(cur, rest, ret):
            if len(cur) == len(nums):
                if cur not in ret:
                    ret.append(cur)
                return 
            for i in range(len(rest)):
                backtrack(cur+[rest[i]], rest[:i]+rest[i+1:], ret)
            return 
        
        backtrack([], nums, ret)
        
        return ret
