"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.
Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true
"""


class Solution:

    def isPalindrome(self, s):

        if s == " ":
            return True

        res = []
        special_character = "[@_!#$%,.\"^&-*;()<>?`+=/\|}'{~:]"
        for i in s:
            if i in special_character or i == " ":
                pass
            else:
                res.append(i.lower())

        new_lst = res[::-1]

        print(res)
        print(new_lst)

        if res == new_lst:
            return True
        return False


def main():
    sol = Solution()
    print(sol.isPalindrome("Marge, let's \"[went].\" I await {news} telegram."))


if __name__ == '__main__':
    main()
