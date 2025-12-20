class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write, read, k = 2, 3, len(nums)
        if k <= 2:
            return k
        for read in range(2, k):
            if nums[read] != nums[write-2]:
                nums[write] = nums[read]
                write +=1

        return write 



