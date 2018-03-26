class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        line, s = 0, 0
        lenth = len(S)
        flag = ord('a')
        for c in S:
            if c == 'a':
                add = widths[0]
            else:
                add = widths[ord(c) - flag]
            if add + s > 100:
                line += 1
                s = add
            else:
                s += add

        return [line + 1, s]