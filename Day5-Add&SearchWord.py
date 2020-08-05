"""
Design a data structure that supports the following two operations:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
"""


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        if not self.children.get(len(word)):
            self.children[len(word)] = [word]

        else:
            self.children[len(word)].append(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if not self.children.get(len(word)):
            return False

        curr = self.children[len(word)]

        for i in range(len(curr)):

            currWord = curr[i]
            flag = True

            for j in range(len(currWord)):

                if currWord[j] == word[j] or word[j] == '.':
                    continue

                else:
                    flag = False

            if flag:
                return True

        return False


def main():
    # Your WordDictionary object will be instantiated and called as such:
    obj = WordDictionary()
    obj.addWord("bad")
    obj.addWord("dad")
    obj.addWord("mad")
    print(obj.search("pad"))
    print(obj.search("bad"))
    print(obj.search(".ad"))
    print(obj.search("b.."))
