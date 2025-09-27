from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))

            print(key)
            #anagrams[key] = word
            anagrams[key].append(word)
        return ( list(anagrams.values()))

        