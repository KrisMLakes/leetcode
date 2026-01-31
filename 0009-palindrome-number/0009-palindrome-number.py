class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y = 0
        og = x
        while x > 0:
            reminder = x%10
            x = x//10
            y = y*10 + reminder
            print (reminder, x, y)
        if og == y:
            return True
        else:
            return False


            
        