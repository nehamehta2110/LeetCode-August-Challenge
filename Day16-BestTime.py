"""
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.
Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
"""


class Solution:
    @staticmethod
    def maxProfit(prices) -> int:
        if not prices:
            return 0

        max_profit = 0
        curr = prices[-1]

        for i in range(len(prices) - 2, -1, -1):

            if prices[i] >= curr:
                curr = prices[i]

            else:
                min_counter = prices[0]
                max_counter = 0

                for j in prices[0:i]:
                    if min_counter > j:
                        min_counter = j
                    elif j - min_counter > max_counter:
                        max_counter = j - min_counter

                profit = curr - prices[i] + max_counter

                if max_profit < profit:
                    max_profit = profit

        return max_profit


def main():
    solve = Solution()
    s = solve.maxProfit([3, 3, 5, 0, 0, 3, 1, 4])
    print(s)


if __name__ == '__main__':
    main()
