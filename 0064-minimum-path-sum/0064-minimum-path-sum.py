class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
        m , n = len(grid) , len(grid[0])
        @cache
        def dp(row, col):
            #total = 0
            if row == 0 and col == 0:
                return grid[0][0]
            if row < 0 or col < 0:
                return float('inf')
            #total = 0
            #if row > 0 and col > 0:
               # total = 
            #elif row 
            return grid[row][col]+ min(dp(row-1, col), dp(row, col-1)) 


        



        return dp(m-1, n-1)