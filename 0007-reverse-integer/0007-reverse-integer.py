class Solution:
    def reverse(self, x: int) -> int:
        i = 0
        arr = []
        neg = 1
        if x == 0:
            return x
        if x < 0:
            neg = -1
            x = neg*x
        while x > 0:
            arr.append(x%10)
            x = int( x / 10)
            i += 1
            #print (i, x, arr)
        x = neg*int("".join(map(str,arr)))
        if -2**31 <= x <= 2**31 + 1:
            return x
        else:
            return 0
        
        