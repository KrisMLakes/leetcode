class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # The logic: If the price tomorrow is higher than today, "buy" today and "sell" tomorrow. If the price goes up again the day after, "buy" again and "sell" again. Adding up all these small gains results in the maximum possible total profit.

        # 2nd, 1/10/26; saw logic trick
        min_price = float('inf')
        max_profit = 0
        i = 1
        while i < len(prices):

            if prices[i] - prices[i-1] > 0:
                max_profit += prices[i] - prices[i-1] 
            i +=1
        return max_profit

        