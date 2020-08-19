"""
Goat Latin
A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.
We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin)
"""


class Solution:
    @staticmethod
    def toGoatLatin(S: str):
        S = S.split()
        for i in range(len(S)):

            if S[i].startswith('a') or S[i].startswith('e') or S[i].startswith('i') or S[i].startswith('o') or S[
                i].startswith('u') or S[i].startswith('A') or S[i].startswith('E') or S[i].startswith('I') or S[
                i].startswith('O') or S[i].startswith('U'):

                S[i] = str(S[i]) + 'ma' + ('a' * (i + 1))

            else:

                S[i] = str(S[i])[1:] + str(S[i])[0] + 'ma' + ('a' * (i + 1))

        S = ' '.join(S)
        return S


def main():
    solve = Solution()
    s = solve.toGoatLatin("I speak Goat Latin")
    print(s)


if __name__ == '__main__':
    main()
