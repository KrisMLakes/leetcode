class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        def valid(x,y):
            return 0<=x<m and 0<=y<n and mat[x][y] == 1

        seen = set()
        m = len(mat)
        n = len(mat[0])
        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0 :
                    queue.append((i,j,1))
                    seen.add((i,j))
        while queue:
            x, y, steps = queue.popleft()
            for dx, dy in directions:
                next_row, next_col = x+dx, y+dy
                if valid(next_row,next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, steps+1))
                    mat[next_row][next_col] = steps
        return mat
