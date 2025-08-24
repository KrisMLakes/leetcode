
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        ans, i = 0, 0
        for boxes, units in boxTypes:
             
            can_fit = min(truckSize-i, boxes)
            ans += can_fit*units
            i += can_fit
            if i > truckSize:
                #ans += ((truckSize-i))*units
                break
        return ans
            
            
        