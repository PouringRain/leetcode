# coding='utf-8'
# level:medium
# 思路：字典树


class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """

        class Trie_node():
            def __init__(self):
                self.word = False
                self.child = {}

        class Trie():
            def __init__(self):
                self.root = Trie_node()

            def add(self, word):
                if word:
                    p = self.root
                    for w in word:
                        if w not in p.child:
                            p.child[w] = Trie_node()
                        p = p.child[w]

                    p.word = True

            def reshape_word(self, word):
                mysentence = ''
                p = self.root
                for w in word:
                    if w in p.child:
                        mysentence += w
                        p = p.child[w]
                        if p.word == True:
                            return mysentence
                    else:
                        break
                return word

        T = Trie()
        result = []
        for word in dict:
            T.add(word)
        for word in sentence.split():
            result.append(T.reshape_word(word))

        return ' '.join(result)


if __name__ == '__main__':
    ans = Solution()
    print(ans.replaceWords(dict = ["cat", "bat", "rat"],
        sentence = "the cattle was rattled by the battery"))
