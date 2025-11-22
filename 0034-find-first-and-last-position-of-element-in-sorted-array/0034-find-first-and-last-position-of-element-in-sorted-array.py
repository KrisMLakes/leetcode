class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums, target):

            left, right = 0, len(nums)-1
            while left < right:
                mid = (left + right)//2
                if target <= nums[mid]:
                    right = mid
                else:
                    left = mid+1
            return left
        
        def findRight(nums, target):
            left, right = 0, len(nums)-1
            while left < right:
                mid = (left+right+1)//2
                if target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid
            return left
        if not nums:
            return [-1,-1]
        first = findFirst(nums, target)
        if nums[first] != target or len(nums) <= first:
            first = -1
        last = findRight(nums, target)
        if nums[last] != target:
            last = -1
        
        return [first,last ]

        