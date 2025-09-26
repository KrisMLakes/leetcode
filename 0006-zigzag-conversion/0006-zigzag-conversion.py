class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigrows = [""]*numRows
        #print(zigrows)
        if numRows == 1 or numRows > len(s):
            return s
        cur_row, step = 0, -1

        for i in s:
            zigrows[cur_row] += i
            #print(i)
            if cur_row == 0 or cur_row == (numRows)-1:
                step *=-1
            cur_row +=step
            #print(zigrows)
            #print(cur_row)
        return "".join(zigrows)
        