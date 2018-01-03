# level: medium

class Solution:
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        l_heights = len(heights)
        k, v = K, V
        while v > 0:
            minpos = -1  # the pos to pour water

            for i in range(k - 1, -1, -1):
                if heights[i] < heights[i + 1]:
                    minpos = i
                elif heights[i] > heights[i + 1]:
                    break

            if minpos != -1:
                heights[minpos] += 1
                v -= 1
                continue

            for i in range(k + 1, l_heights):
                if heights[i] < heights[i - 1]:
                    minpos = i
                elif heights[i] > heights[i - 1]:
                    break
            if minpos != -1:
                heights[minpos] += 1
                v -= 1
                continue

            else:
                heights[k] += 1
                v -= 1


        return heights

if __name__ == '__main__':
    ans = Solution()
    print(ans.pourWater([2,1,1,2,1,2,2],4,3))