class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least = prices[0]
        profit = 0

        for n in prices:

            profit = max(profit, n - least)

            if n < least:
                least = n

        return profit
                

        