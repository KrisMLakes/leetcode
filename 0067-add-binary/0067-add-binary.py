class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a,2)
        y = int(b,2)

        while y:
            sum_ = x ^ y
            carry = (x & y) << 1
            x, y = sum_, carry
        
        return bin(x)[2:]
        