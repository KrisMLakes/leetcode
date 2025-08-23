class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        smallpairs = []
        sums = []

        for i in range(min(k, len(nums1))):
            heapq.heappush(sums, (nums1[i]+nums2[0], i, 0))

        while sums and len(smallpairs) <k :
            smallsum, i , j = heapq.heappop(sums)
            smallpairs.append((nums1[i],nums2[j]))
            if j+1 < len(nums2):
                heapq.heappush(sums, (nums1[i]+nums2[j+1], i, j+1) )
        return smallpairs



        