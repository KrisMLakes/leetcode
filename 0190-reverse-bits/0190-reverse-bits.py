class Solution:
    def reverseBits(self, n: int) -> int:
        x = bin(n)[2:].zfill(32)
        c = ''.join(reversed(str(x)))
        return int(c,2)
        