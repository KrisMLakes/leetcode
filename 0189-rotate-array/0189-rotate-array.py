class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        2nd, chatgpt, 12/20/25
        3rd, 1/10/2026
        """
        k %=len(nums)

        def reverse(nums: List[int], n1: int, n2: int):
            j = n2# = len(nums)
            for i in range(n1,int(n1 + (n2-n1)/2)):
                nums[i], nums[j-1] = nums[j-1], nums[i]
                j -=1
        reverse(nums, 0, len(nums))
        #print (nums)
        reverse(nums, 0, k)
        #print (nums)
        reverse(nums, k, len(nums))
        

        