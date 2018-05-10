# level: eazy
# solution: stack

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '': return True
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            elif s[i] == '[':
                stack.append(s[i])
            elif s[i] == '{':
                stack.append(s[i])
            elif s[i] == ')':
                if stack and stack.pop() == '(':
                    continue
                else:
                    return False
            elif s[i] == '}':
                if stack and stack.pop() == '{':
                    continue
                else:
                    return False
            elif s[i] == ']':
                if stack and stack.pop() == '[':
                    continue
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
