class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_map = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz"
        }
        

        def backtrack(idx, curr):
            
            if idx == len(digits):
                lettermap.append("".join(curr))
                return
            dig = digits[idx]
            
            letters = digit_map[dig]
            
            for letter in letters:
                curr.append(letter)
                backtrack(idx+1, curr)
                curr.pop()

        lettermap = []
        backtrack(0,[])
        return lettermap