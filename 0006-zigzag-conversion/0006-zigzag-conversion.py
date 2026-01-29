class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #3rd: 1/29: mostly own, remembered from weekend review
        if numRows == 1 or len(s) == 1:
            return s
        zigrows = [""]*numRows
        step = -1
        j = 0
        for i in s:
            zigrows[j] +=i
            if j == 0 or j == numRows-1:
                step *=-1
            j +=step
        return "".join(zigrows)
