import heapq
from typing import List

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # Convert to max heap (negative values)
        piles = [-pile for pile in piles]
        heapq.heapify(piles)

        for _ in range(k):
            maxpile = -heapq.heappop(piles)
            reduced = maxpile - (maxpile // 2)  # remove floor(maxpile/2)
            heapq.heappush(piles, -reduced)

        total = 0
        while piles:
            total += -heapq.heappop(piles)
        return total