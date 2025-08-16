class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def validrow(x,y):
            return 0<= x< m and 0<= y< n and grid[x][y] == 1
        
        def dfs(x,y):
            area = 1
            for dx,dy in directions:
                
                next_row, next_col = x+dx, y+dy
                if validrow(next_row, next_col) and (next_row,next_col) not in seen:
                    seen.add((next_row, next_col))
                    area += dfs(next_row, next_col)
                    
            return area
            
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        max_ans = 0
        seen = set()
        m = len(grid)
        n = len(grid[0])
        for row in range(m):
            for col in range(n):
                if grid[row][col]==1 and (row,col) not in seen:
                    seen.add((row,col))
                    max_ans = max(max_ans, dfs(row,col))
                    
                    
            
        return max_ans
        