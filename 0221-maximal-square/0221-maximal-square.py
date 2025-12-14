class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        


        @cache
        def findMaxSide(row,col):
            
            if row < 0 or col < 0:
                return 0
            if matrix[row][col]=='0':
                return 0
            return min(findMaxSide(row-1,col), findMaxSide(row,col-1), findMaxSide(row-1,col-1)) +1
            



        max_side = 0
        for i in range(m):
            for j in range(n):
                max_side = max(max_side, findMaxSide(i,j))



        return max_side * max_side 
        