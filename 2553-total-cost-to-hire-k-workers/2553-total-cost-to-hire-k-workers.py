import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        fheap = []
        bheap = []
        total = 0
        n = len(costs)
        l, r = 0, n-1
        for _ in range(candidates):
            if l <= r:
                heapq.heappush(fheap, costs[l])
                l +=1
        print(fheap)
        for _ in range(candidates):
            if l <= r:
                heapq.heappush(bheap, costs[r])
                r -=1
        print(bheap)
        for _ in range(k):
            if not bheap or ( fheap and fheap[0] <= bheap[0]):
                total += heapq.heappop(fheap)
                
                if l <= r:
                    heapq.heappush(fheap, costs[l])
                    l +=1
            else:
                total +=heapq.heappop(bheap)
                
                if l <= r:
                    heapq.heappush(bheap, costs[r])
                    r -=1
        
        return total