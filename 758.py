class Solution(object):
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        l_s = len(S)
        t = [0] * l_s
        for word in words:
            l_w = len(word)
            p = S.find(word)
            while p != -1:
                for i in range(p, p + l_w):
                    t[i] = 1
                p = S.find(word, p + 1)
        print t

        i, ans = 0, ''
        while i < l_s:
            if t[i]:
                ans += r'<b>'
                while i < l_s and t[i]:
                    ans += S[i]
                    i += 1
                ans += r'</b>'
            else:
                ans += S[i]
                i += 1

        return ans