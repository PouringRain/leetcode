class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        # print(ord('a'))
        t = ord(target)
        for i, letter in enumerate(letters):
            if t < ord(letter):
                return letter

        return letters[0]

if __name__ == '__main__':
    ans = Solution()
    print(ans.nextGreatestLetter(["c", "f", "j"], 'a'))