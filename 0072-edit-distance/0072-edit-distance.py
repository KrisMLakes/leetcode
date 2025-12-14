class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        

        @cache
        def dp(i,j):

            if i == 0:
                return j
            if j ==0:
                return i
            if word1[i-1] == word2[j-1]:
                return dp(i-1,j-1)
            else:
                insert_cost = dp(i-1, j) +1
                delete_cost = dp(i, j-1) +1
                replace_cost = dp(i-1,j-1) +1
                return min(insert_cost, delete_cost, replace_cost)






        return dp(len(word1), len(word2))