class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        x, y = target[0], target[1]
        p = abs(x) + abs(y)
        
        for ghost in ghosts:
            dis_g = abs(ghost[0] - x) + abs(ghost[1] - y)
            if p >= dis_g:
                return False

        return True
