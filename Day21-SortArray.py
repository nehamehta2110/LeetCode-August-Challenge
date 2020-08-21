"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
"""


class Solution:
    @staticmethod
    def sortArrayByParity(A):
        n = len(A)
        i = -1
        j = 0
        while j != n:
            if A[j] % 2 == 0:
                i = i + 1
                A[i], A[j] = A[j], A[i]
            j = j + 1
        return A


def main():
    solve = Solution()
    print(solve.sortArrayByParity([3, 1, 2, 4]))


if __name__ == '__main__':
    main()
