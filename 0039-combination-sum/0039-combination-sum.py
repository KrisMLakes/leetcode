class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(startidx, curr):
            if sum(curr) == target:
                ans.append(curr[:])
                return
            if sum(curr) > target:
                return
            else:
                for i in range(startidx, len(candidates)):
                    if candidates[i]+sum(curr) > target:
                        break
                    curr.append(candidates[i])
                    backtrack(i, curr)
                    curr.pop()
        ans = []
        backtrack(0,[])
        return ans
        