class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        visited = {beginWord}

        q = deque([(beginWord,1)])
        letters = set(list(beginWord))
        for each in wordSet:
            letters.update(list(each))



        while q:
            currWord, steps = q.popleft()
            if currWord == endWord:
                return steps
            for i in range(len(currWord)):
                for each in letters:
                    nextWord = list(currWord)
                    nextWord[i] = each
                    nextWord = "".join(nextWord)
                    if nextWord in wordSet and nextWord not in visited:
                        q.append((nextWord, steps+1))
                        visited.add(nextWord)
        return 0
        