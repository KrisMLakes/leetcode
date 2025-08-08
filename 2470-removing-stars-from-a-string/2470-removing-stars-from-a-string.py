class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        i = ""
        #print(list(s))
        for i in list(s):
            #print(i)
            if i == "*":
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
        