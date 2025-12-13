class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache

        def dp(i,hold):
            if i == len(prices):
                return 0
            if hold:
                arr = max(dp(i+1, hold), prices[i]-fee+dp(i+1, False))
            
            else:
                arr = max(dp(i+1, hold), dp(i+1, True)-prices[i])
            return arr







        return dp(0,False)
        