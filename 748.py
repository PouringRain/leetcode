class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        # minlen:shortest lenth

        minlen = 15
        result = ''
        count = dict()
        for c in licensePlate:
            if c.isalpha():
                c = c.lower()
                if c not in count:
                    count[c] = 0
                count[c] += 1

        for word in words:
            flag = 1
            i_count = count.copy()
            print i_count
            for c in word:
                if i_count.has_key(c):
                    if i_count[c] != 0:
                        i_count[c] -= 1

            for key, val in i_count.items():
                if val != 0:
                    flag = 0
            if flag and len(word) < minlen:
                minlen, result = len(word), word

        return result
if __name__ == '__main__':
    ans = Solution()
    print(ans.shortestCompletingWord("1s3 PSt",
            ["step","steps","stripe","stepple"]))