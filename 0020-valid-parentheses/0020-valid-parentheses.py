class Solution:
    def isValid(self, s: str) -> bool:
        stack1 = []
        matching = {'}':'{',']':'[',')':'('}
        for c in s:
            #print(c)
            if c in matching:
                if not stack1 or stack1[-1] != matching[c]:
                    return False
                
                stack1.pop()
                #print(stack1)
            else:
                stack1.append(c)
            #print(stack1)
        return not stack1
        