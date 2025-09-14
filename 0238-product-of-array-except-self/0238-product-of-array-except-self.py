class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1]*n
        prefix, postfix = 1, 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        for j in range(n-1, -1, -1):
            answer[j] *= postfix
            postfix *= nums[j]

        return answer

