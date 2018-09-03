class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        candidates.sort()
        # print candidates
        def backtrack(cur, rest, start, candidates, ret):
            if rest<0:
                return
            elif rest==0:
                if cur not in ret:
                    ret.append(cur)
                return 
            else:
                for i in range(start, len(candidates)):
                    backtrack(cur+[candidates[i]], rest-candidates[i], i+1, candidates, ret)
        
        backtrack([], target, 0, candidates, ret)
        return ret
