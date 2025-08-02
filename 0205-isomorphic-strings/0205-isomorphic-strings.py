class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq1 = defaultdict(list)
        freq2 = defaultdict(list)
        for i in range(len(s)):
            freq1[s[i]].append(i)
            freq2[t[i]].append(i)

        #print(freq1, freq2)
        for j in range(len(s)):
            if freq1[s[j]] != freq2[t[j]]:
                return False
        return True

        