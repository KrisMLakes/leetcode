class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0]*n
        j = 0
        product = 1
        arr = []
        for i in range(n):
            if nums[i] == 0:
                arr.append(i)
                j +=1
            else:
                product *=nums[i]
                #print (product)
        print (j, product, arr)
        if j > 1:
            return answer
        elif j == 1:
            answer[arr[0]] = product
            return answer
        else:
            for i in range(n):
                answer[i] = int(product/nums[i])
            return answer


