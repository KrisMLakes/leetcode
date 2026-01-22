class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort(reverse=True)
        i = 0
        while i <= len(citations)-1:
            if i+1 > citations[i] :
                break
            else:
                i +=1
        return i
#6, 5, 3, 1, 0
