"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
Example 1:
Input: 16
Output: true
"""


class Solution:
    def isPowerOfFour(self, num):
        return num != 0 \
               and ((num & (num - 1)) == 0) \
               and not (num & 0xAAAAAAAA)

        # or
        # return n!=0 and math.floor(math.log(num,4)) == math.ceil(math.log(num,4)


def main():
    solve = Solution()
    print(solve.isPowerOfFour(int(input("Enter number"))))


if __name__ == '__main__':
    main()
