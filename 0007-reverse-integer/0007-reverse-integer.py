class Solution:
    def reverse(self, x: int) -> int:
        #1st attempt, 1/24 Own solution  ( leetcode does math based, I did string based)
        #3rd, 1/31; 2nd on paper
        if -9 <= x <= 9:
            return x
        step = 1
        if x < 0:
            step = -1
            x *= step
        y = 0
        while x > 0:
            reminder = x % 10
            x = x//10
            
            y = y*10 + reminder
            #print (reminder, x, y)
        y *=step
        if -2**31 <= y <= 2**31-1:
            return y
        else:
            return 0
        