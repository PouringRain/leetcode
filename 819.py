# level: eazy

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        s = paragraph.lower()
        slist = s.split()
        for i, word in enumerate(slist):
            for c in word:
                if not c.isalpha():
                    slist[i] = word[:-1]

        d = collections.Counter(slist)
        for key in banned:
            d[key] = -1
        m, ans = -1, ''
        for k, v in d.items():
            if m <= v:
                ans = k
                m = v
        return ans