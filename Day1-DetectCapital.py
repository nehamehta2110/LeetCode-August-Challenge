"""
Detect Capital
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.

"""


class Solution:

    def __init__(self, word):
        self.word = word

    def detectCapitalUse(self):
        if self.word.isupper():
            return True

        elif self.word.islower():
            return True

        elif self.word[0].isupper() and self.word[1:].islower():
            return True

        else:
            return False


def main():
    t = int(input())
    while t != 0:
        wrd = input("enter string")
        sol = Solution(wrd)
        print(sol.detectCapitalUse())
        t -= 1


if __name__ == '__main__':
    main()
