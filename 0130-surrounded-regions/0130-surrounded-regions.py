class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        rows, cols = len(board), len(board[0])
        def dfs(r,c):
            if (r-1 >= 0 and board[r-1][c]=="O"):
                board[r-1][c]="T"
                dfs(r-1,c)
            if (r+1 <rows and board[r+1][c]=="O"):
                board[r+1][c]="T"
                dfs(r+1,c)
            if (c-1 >= 0 and board[r][c-1]=="O"):
                board[r][c-1]="T"
                dfs(r,c-1)
            if (c+1 <cols and board[r][c+1]=="O"):
                board[r][c+1]="T"
                dfs(r,c+1)
        for i in range(rows):
            if board[i][0] == "O":
                board[i][0]="T"
                dfs(i,0)
            if board[i][cols-1]=="O":
                board[i][cols-1]="T"
                dfs(i,cols-1)
        for j in range(cols):
            if board[0][j] == "O":
                board[0][j]="T"
                dfs(0,j)
            if board[rows-1][j]=="O":
                board[rows-1][j]="T"
                dfs(rows-1,j)         


        for i in range(rows):
            for j in range(cols):
                if (i !=0 and i != rows-1 and j !=0 and j != cols-1):
                    if board[i][j]=="O":
                        board[i][j]="X"
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "T":
                    board[i][j] = "O"
        return


