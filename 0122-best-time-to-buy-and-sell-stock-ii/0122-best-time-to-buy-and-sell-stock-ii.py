class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #min_price = float('inf')
        profit = 0
        
        for i in range(1, len(prices)): 
            if prices[i] > prices[i-1]: # min_price:
                profit += prices[i]-prices[i-1]
        return profit
        