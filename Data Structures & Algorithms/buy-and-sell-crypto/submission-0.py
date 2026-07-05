class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price  = prices[0]   # cheapest price seen so far
        max_profit = 0           # best profit seen so far

        for price in prices:                         # walk through every day

            if price < min_price:                    # found a cheaper buy day
                min_price = price

            profit = price - min_price               # profit if we sell today
            max_profit = max(max_profit, profit)     # update best profit

        return max_profit
        