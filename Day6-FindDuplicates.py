"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array),
some elements appear twice and others appear once. Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?
Input:[4,3,2,7,8,2,3,1]
Output:[2,3]
"""


class Solution:
    def findDuplicates(self, nums):

        arr = []
        for i in range(0, len(nums)):

            if nums[abs(nums[i]) - 1] >= 0:
                nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]
            else:
                arr.append(abs(nums[i]))

        return arr


def main():
    solve = Solution()
    print(solve.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))


if __name__ == '__main__':
    main()
