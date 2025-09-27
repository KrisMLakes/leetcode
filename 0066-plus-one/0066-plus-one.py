class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #i = len(digits)
        num = int(''.join(map(str, digits)))
        return [int(digit) for digit in str(num+1)]
        #if digits[i]
        #digits[i] +=
        