class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        m = len(triangle)
        n = len(triangle[m-1])

        @cache
        def dp(row, col):
            if row == m-1:
                return triangle[row][col]
            #for j in range(row+1)
            ans = triangle[row][col] + min(dp(row+1,col), dp(row+1, col+1))
            return ans


        return dp(0,0)
        