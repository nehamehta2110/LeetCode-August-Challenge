"""
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
"""


class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])
        i = 1
        answer = 0
        while i < len(intervals):
            if intervals[i][0] < intervals[i - 1][1]:
                intervals.pop(i)
                answer += 1
            else:
                i += 1
        return answer


if __name__ == '__main__':
    solve = Solution()
    s = solve.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]])
    print(s)