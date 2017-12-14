class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """

        # func: start/end : time
        stack = []
        result = [0] * n
        t = logs[0].split(':')
        i, prev = 1, int(t[2])
        stack.append(t[0])
        while i < len(logs):
            t = logs[i].split(':')

            if t[1] == 'start':
                if stack:
                    result[int(stack[-1])] += int(t[2]) - prev
                prev = int(t[2])
                stack.append(t[0])

            elif t[1] == 'end':
                result[int(stack[-1])] += int(t[2]) - prev + 1
                stack.pop()
                prev = int(t[2]) + 1
            i += 1

        return result

if __name__ == '__main__':
    ans = Solution()
    print(ans.exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]))