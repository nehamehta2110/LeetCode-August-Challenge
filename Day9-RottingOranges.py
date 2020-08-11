"""
In a given grid, each cell can have one of three values:
the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
"""


class Solution:
    def orangesRotting(self, grid):
        def rotting(ro):
            temp = []
            for i, j in ro:
                # top
                if i > 0 and grid[i - 1][j] == 1:
                    temp.append((i - 1, j))
                    grid[i - 1][j] = 2
                # bottom
                if i < l_row - 1 and grid[i + 1][j] == 1:
                    temp.append((i + 1, j))
                    grid[i + 1][j] = 2
                # left
                if j > 0 and grid[i][j - 1] == 1:
                    temp.append((i, j - 1))
                    grid[i][j - 1] = 2
                # right
                if j < l_cols - 1 and grid[i][j + 1] == 1:
                    temp.append((i, j + 1))
                    grid[i][j + 1] = 2
            return temp

        l_row = len(grid)
        l_cols = len(grid[0])

        rotten = [(i, j) for i in range(l_row) for j in range(l_cols) if grid[i][j] == 2]

        count = 0

        while rotten:
            rotten = rotting(rotten)
            if len(rotten) == 0:
                break
            count += 1

        for i in range(l_row):
            for j in range(l_cols):
                if grid[i][j] == 1:
                    return -1

        return count


def main():
    inp = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]

    solve = Solution()
    print(solve.orangesRotting(inp))


if __name__ == '__main__':
    main()
