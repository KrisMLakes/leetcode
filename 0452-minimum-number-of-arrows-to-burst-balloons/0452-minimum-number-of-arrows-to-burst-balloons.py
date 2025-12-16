class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()

        res = []

        for start, end in points:
            if res and res[-1][1] >= start:
                
                res[-1][1] = min(end, res[-1][1])
            else:
                res.append([start, end])



        return len(res)
        