class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        arr = []
        for start, end in intervals:
            if arr and arr[-1][1] >= start:
                arr[-1][1] = max(end, arr[-1][1])
            else:
                arr.append([start,end])
        return arr
        