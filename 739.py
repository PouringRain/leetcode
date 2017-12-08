# coding=utf-8

# difficult: Medium
# temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# output = [1, 1, 4, 2, 1, 1, 0, 0].
# 题目：找出到晴天最近的距离
# 思路：set结构存储天气和序号，每新到的天气，将比他小的天气最小距离求差。 普通n方复杂度过不了

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        if not temperatures:
            return []

        result, stack = [0]*len(temperatures), []
        stack.append((temperatures[0], 0))
        for i in range(1, len(temperatures)):
            while stack:
                # 取stack[-1]做比较，因为stack[-1]之前的temperature均大于末位
                p = stack[-1]
                if p[0] < temperatures[i]:
                    result[p[1]] = i-p[1]
                    stack.pop()
                else:
                    break
            stack.append((temperatures[i], i))

        return result

if __name__ == '__main__':
    ans = Solution()
    print(ans.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
