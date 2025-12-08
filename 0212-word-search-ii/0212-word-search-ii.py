
class TrieNode:
    def __init__(self):
            
        self.children = {}
        self.word = None

class Solution:

        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = word
        
        rows, cols = len(board), len(board[0])

        result = []

        for r in range(rows):
            for c in range(cols):
                self.dfs(board, rows, cols, r, c, result, root)
        
        return result


        

    def dfs (self, board, rows, cols, r, c, result, node):

            if r < 0 or r == rows or c < 0 or c == cols:
                return
            char = board[r][c]

            if char == "#":
                return
            if char not in node.children:
                return
            node = node.children[char]
            if node.word is not None:
                result.append(node.word)

                node.word = None

            board[r][c] = "#"
            
            self.dfs(board, rows, cols, r-1, c, result, node)
            self.dfs(board, rows, cols, r+1, c, result, node)
            self.dfs(board, rows, cols, r, c-1, result, node)
            self.dfs(board, rows, cols, r, c+1, result, node)

            board[r][c] = char
            
             