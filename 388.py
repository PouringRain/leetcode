class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        maxlen=curlen= 0
        # ( , )  --> depth, lenth
        stack = [(-1, 0)]
        input = input.split('\n')
        for x in input:
            depth = x.count('\t')
            name = x.replace('\t', '')
            # 栈顶
            tdepth, tlen = stack[-1]
            while depth <= tdepth:
                stack.pop()
                curlen -= tlen
                tdepth, tlen = stack[-1]

            curlen = tlen + len(name)
            stack.append((depth, curlen))

            if name.count('.'):

                maxlen = max(maxlen, curlen+depth)

        return maxlen

if __name__ == '__main__':
    ans = Solution()
    print(ans.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))