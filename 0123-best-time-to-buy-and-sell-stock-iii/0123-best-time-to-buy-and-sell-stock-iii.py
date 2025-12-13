class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(i,hold, remain):
            if i == len(prices) or remain == 0:
                return 0
            
            if hold:
                arr = max(dp(i+1,hold, remain), dp(i+1, False, remain-1)+prices[i])
            else:
                arr = max(dp(i+1, hold, remain), dp(i+1, True, remain)-prices[i])
            return arr




        return dp(0,False,2)
        