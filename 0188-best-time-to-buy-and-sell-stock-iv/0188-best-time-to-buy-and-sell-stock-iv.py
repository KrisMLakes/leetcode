class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @cache
        def dp(i,holding, remain):
            if i==len(prices) or remain ==0:
                return 0
            
            if holding:
                return max(dp(i+1,holding, remain), dp(i+1,False,remain-1)+prices[i])
            else:
                return max(dp(i+1, holding, remain), dp(i+1,True,remain)-prices[i])








        return dp(0,False,k)
        