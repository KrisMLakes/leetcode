class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False

        