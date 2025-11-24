class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])


        def backtrack(r,c,i):
            if len(word) == i:
                return True
            if (r < 0 or r >= row or c < 0 or c >= col or board[r][c] != word[i]):
                return False
            
            temp = board[r][c]
            board[r][c] = "#"
            
            res = (backtrack(r-1, c, i+1) or
                        backtrack(r+1, c, i+1) or
                        backtrack(r, c-1, i+1) or
                        backtrack(r, c+1, i+1))
            

            board[r][c] = temp
            return res 



            
        for i in range(row):
            for j in range(col):
                if word[0] == board[i][j] and backtrack(i,j,0):
                    return True
        return False
        