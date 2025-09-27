class Solution:
    def isValid(self, s: str) -> bool:
        stack1 = []
        matching = {"{":"}","[":"]","(":")"}
        for c in s:
            if c in matching:
                stack1.append(c)
                print(c)
                continue
            else:
                if not stack1:
                    return False
            if matching[stack1.pop()] != c:
                
                return False
        return not stack1
        