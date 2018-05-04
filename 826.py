# level: medium

class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        jobs = zip(difficulty, profit)
        jobs.sort()
        ans = i = best = 0
        lenth = len(difficulty)
        for ability in sorted(worker):
            while i < lenth and ability >= jobs[i][0]:
                best = max(best, jobs[i][1])
                i += 1
            ans += best

        return ans