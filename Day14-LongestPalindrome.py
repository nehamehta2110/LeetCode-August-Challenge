"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
Input:
"abccccdd"
Output:
7
"""

import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        for v in collections.Counter(s).values():
            res += v // 2 * 2
            if res % 2 == 0 and v % 2 == 1:
                res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    result = s.longestPalindrome("abccccdd")
    print(result)
