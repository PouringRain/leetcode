# level: medium
# solution: two pointers

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p, q = 0, len(height) - 1
        maxWater = -1
        while p < q:
            if height[p] <= height[q]:
                cur = (q - p) * height[p]
                if maxWater < cur:
                    maxWater = cur
                p += 1

            else:
                cur = (q - p) * height[q]
                if maxWater < cur:
                    maxWater = cur
                q -= 1

        return maxWater