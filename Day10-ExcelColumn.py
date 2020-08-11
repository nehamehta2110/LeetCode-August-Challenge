"""
Given a column title as appear in an Excel sheet, return its corresponding column number.
For example: A -> 1
             B -> 2
             C -> 3
             ...
             Z -> 26
             AA -> 27
             AB -> 28
"""


class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            result *= 26
            result += ord(s[i]) - ord('A') + 1

        return result


def main():
    solve = Solution()
    print(solve.titleToNumber('AB'))


if __name__ == '__main__':
    main()
