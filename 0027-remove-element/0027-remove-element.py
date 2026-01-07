class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
##""2nd 12/18/2025"
## 3rd 1/7/2026 - Own solution !! yey !!
        k = 0
        n = len(nums)
        if n == 0:
            return 0
        i, j = 0, n-1
        while i < n and i <= j:
            if nums[i] == val and nums[j] != val:
                print (nums[i], nums[j], "before", nums)
                nums[i], nums[j] = nums[j], nums[i]
                print (nums[i], nums[j], "after", nums)
                i += 1
                j -= 1
                k += 1
            elif nums[i] == val and nums[j] == val:
                j -=1
            elif nums[i] != val:
                k +=1
                i +=1 
            print (i, j, j)
        return k
