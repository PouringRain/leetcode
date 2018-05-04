# level: eazy

class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split()
        res = []
        for i, word in enumerate(words):
            if word[0].lower() in ['a', 'e', 'i', 'o', 'u'] or len(word) == 1:
                res.append(word + 'ma' + 'a' * (i + 1))
            else:
                res.append(word[1:] + word[0] + 'ma' + 'a' * (i + 1))

        return ' '.join(res)
