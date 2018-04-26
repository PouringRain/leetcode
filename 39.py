# level: medium
# soluton: backtracking
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        # print candidates
        res = []
        self.backtracking(res, target, 0, [], candidates)
        return res

    def backtracking(self, res, target, start, combination, candidates):
        if target < 0: return
        if target == 0:
            res.append(combination)
            return
        for i in range(start, len(candidates)):
            # print combination, target-candidate
            self.backtracking(res, target - candidates[i], i, combination + [candidates[i]], candidates)