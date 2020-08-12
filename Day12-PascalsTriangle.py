"""
Pascal's Triangle II
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
"""


class Solution:
    def getRow(self, rowIndex):
        triangle = [1]

        for i in range(1, rowIndex + 1):
            triangle.append(int(triangle[i - 1] * (rowIndex - (i - 1)) / i))

        return triangle


def main():
    index = 3
    solve = Solution()
    print(solve.getRow(3))


if __name__ == '__main__':
    main()

