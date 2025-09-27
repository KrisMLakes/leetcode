class Solution:
    def isHappy(self, n: int) -> bool:
        def sumsquare (n:int) -> int:
            digits = []
            sum_square = 0
            while n > 0:
                digits.append(n%10)
                n = n//10
            for i in digits:
                sum_square += i*i
            return sum_square 
        sums = n
        lastseen = set()
        if n == 1:
            return True

        while sums > 1:
            sums = sumsquare(sums)
            if sums in lastseen:
                return False
            lastseen.add(sums)

            print (sums)
            if sums == 1:
                return True

        