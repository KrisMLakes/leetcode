class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 2nd: 1/31, own solution
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


            
       # 2. Early exit optimization (common interview improvement)

#You can avoid reversing the entire number. Instead, reverse only half of it.

#Example:

#1221

#Left: 12

#Right reversed: 12

#This reduces work and avoids overflow issues in languages like Java/C++.

#⭐ Industry-Standard Optimal Solution (Half Reversal)
#class Solution:
 #   def isPalindrome(self, x: int) -> bool:
 #       if x < 0 or (x % 10 == 0 and x != 0):
#            return False

 #       rev = 0
 #       while x > rev:
 #           rev = rev * 10 + x % 10
 #           x //= 10

 #       return x == rev or x == rev // 10