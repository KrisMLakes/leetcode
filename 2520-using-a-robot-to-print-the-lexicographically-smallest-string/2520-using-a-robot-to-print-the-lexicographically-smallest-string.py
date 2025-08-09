class Solution:
    def robotWithString(self, s: str) -> str:
        smallest_stack = [0]*len(s)
        smallest = chr(ord("z")+1)
        t = []
        result = []

        for i in range( len(s)-1, -1, -1):
            smallest = min(smallest, s[i])
            smallest_stack[i] = smallest

        for i, ch in enumerate(s):
            t.append(ch)
            while t and (i == len(s)-1 or  t[-1] <= smallest_stack[i+1]):
                result.append(t.pop())
        
        return "".join(result)


        