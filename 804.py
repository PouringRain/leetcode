class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        res = set()
        flag = ord('a')
        for word in words:
            s = ''
            for c in word:
                if c == 'a':
                    s += morse[0]
                else:
                    s += morse[ord(c) - flag]

            res.add(s)

        return len(res)