# level: medium
# solution: stack

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [['', 1]]
        num = ''
        for c in s:
            if c.isdigit():
                num += c
            elif c == '[':
                stack.append(['', int(num)])
                num = ''
            elif c == ']':
                seq, n = stack.pop()
                stack[-1][0] += seq * n
            else:
                stack[-1][0] += c

        return stack[-1][0]