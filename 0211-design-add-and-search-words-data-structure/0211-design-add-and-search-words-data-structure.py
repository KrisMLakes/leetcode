class WordDictionary:

    def __init__(self):
        self.children = { }
        self.is_end = False
        

    def addWord(self, word: str) -> None:
        curr = self #self = WordDictionary()
        for c in word:
            
            if c not in curr.children:
                curr.children[c] = WordDictionary() #curr.children[c]
            curr = curr.children[c]
        curr.is_end = True
            

    def search(self, word: str) -> bool:
        curr = self

        def dfs(index, node):
            if index == len(word):
                return node.is_end
            
            c = word[index]
            if c ==".":
                for d in node.children:
                    if dfs(index+1,node.children[d] ):
                        return True
                return False
            if c not in node.children:
                return False
            
            return dfs(index+1, node.children[c])
        
        return dfs(0,self)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)