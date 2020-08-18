"""
Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.
Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
"""


class Solution:
    def numsSameConsecDiff(self, N: int, K: int):
        if N == 1:
            return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = []
        stack = [[1], [2], [3], [4], [5], [6], [7], [8], [9]]
        while stack:
            n = stack.pop()
            k = n[:]
            i = n[len(n) - 1]
            if 0 <= i - K < 10:
                n.append(i - K)

                if len(n) == N:
                    result.append(''.join(map(str, n)))
                else:
                    stack.append(n)

            if K + i < 10 and (i - K != K + i):
                k.append(K + i)

                if len(k) == N:
                    result.append(''.join(map(str, k)))
                else:
                    stack.append(k)

        return result


def main():
    solve = Solution()
    s = solve.numsSameConsecDiff(3, 7)
    print(s)


if __name__ == '__main__':
    main()
