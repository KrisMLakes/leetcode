class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache

        def dp(i,hold):
            if i >= len(prices):
                return 0
            
            if hold:
                arr = max(dp(i+1,hold), dp(i+2,False)+prices[i])
            #elif sold:
                #arr = dp(i+1, False, False)
            
            else:
                arr = max(dp(i+1,False), dp(i+1, True)-prices[i])
            return arr












        return dp(0,False)
        