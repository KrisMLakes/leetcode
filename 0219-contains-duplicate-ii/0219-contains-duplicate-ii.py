from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices = defaultdict(list)
        for i in range(len(nums)):
            key = nums[i]
            indices[key].append(i)

        for key in indices.keys():
            inde = list(indices[key])
            if len(inde) > 1:
                for j in range(1,len(inde)):
                    if inde[j] - inde[j-1] <= k:
                        return True
        return False
        