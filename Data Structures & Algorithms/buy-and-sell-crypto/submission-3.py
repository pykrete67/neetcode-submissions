class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: # edge case
            return 0
        
        least = prices[0]
        profit = 0

        for n in prices:

            profit = max(profit, n - least)

            if n < least:
                least = n

        return profit
                

        