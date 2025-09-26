class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        #print(words)
        return " ".join(words)
        