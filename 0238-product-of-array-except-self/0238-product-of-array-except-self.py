class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1/24 2nd: own solution in 21 minutes; missed the constraint, then saw solution
        # idea: product of left * product of right
        n = len(nums)

        answer = [1]*n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer

