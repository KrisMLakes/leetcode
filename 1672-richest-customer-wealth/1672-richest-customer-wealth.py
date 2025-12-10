class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        r, c = len(accounts), len(accounts[0])
        maxwel = 0

        for i in range(r):
            maxwel = max(maxwel, sum(accounts[i]))
        return maxwel
        