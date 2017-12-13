# level: eazy

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        row1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        row2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        row3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        for word in words:
            result.append(word)
            word = word.lower()
            if word[0] in row1:
                row = row1.copy()
            elif word[0] in row2:
                row = row2.copy()
            else:
                row = row3.copy()
            # print(row)
            for i, c in enumerate(word):
                if c not in row:
                    result.pop()
                    break

        return result

if __name__ == '__main__':
    ans = Solution()
    print(ans.findWords(["Hello","Alaska","Dad","Peace"]))
