class Solution:
    # 2nd 12/22/25 - can solve with - time limit exceeded; chatgpt - optimal
    # 3rd 1/10/26 - time limit exceeded - two pointer didnt work
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = float(inf)

        for price in prices:
            if price < minPrice:
                minPrice = price
            if price - minPrice > maxProfit:
                maxProfit = price - minPrice

        return maxProfit
        
