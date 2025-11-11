class Solution:
    def hammingWeight(self, n: int) -> int:
        #x = bin(n)[2:]
        y = 0

        while n:
            if n & 1 == 1:
                y+=1
            n >>=1
        return y