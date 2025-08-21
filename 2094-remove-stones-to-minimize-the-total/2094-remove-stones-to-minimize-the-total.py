import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles)
        i = 0
        while i < k:
            maxpile = abs(heapq.heappop(piles))
            heapq.heappush(piles, -(maxpile - maxpile//2))
            i += 1
        
        pilesum = 0
        while len(piles) > 0:
            pilesum += -heapq.heappop(piles)
            
        return pilesum
        