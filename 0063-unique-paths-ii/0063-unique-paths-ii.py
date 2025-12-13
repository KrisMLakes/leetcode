class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        @cache
        def dp(row, col):
            if obstacleGrid[row][col] == 1:
                return 0
            if (row == 0 and col == 0):
                return 1
            ways = 0
            if row > 0 and obstacleGrid[row-1][col] == 0:
                ways += dp(row-1, col)
            if col > 0 and obstacleGrid[row][col-1] == 0:
                ways += dp(row, col-1)
            return ways








        return dp(m-1, n-1)
        