class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        if endGene not in bank:
            return -1
        genes = ['A', 'C','T','G']
        # distance
        # while q
        #popleft()
        #q.append()
        #return -1
        bankSet = set(bank)
        visited = {startGene}
        q = deque([(startGene,0)])

        #for each in bank:





        while q:
            currGene, steps = q.popleft()
            if currGene == endGene:
                return steps
            for i in range(len(currGene)):
                
                for gene in genes:
                    nextGene = list(currGene)
                    nextGene[i] = gene
                    nextGene = "".join(nextGene)
                    
                    if nextGene in bankSet and nextGene not in visited:
                        #print (nextGene)
                        q.append((nextGene, steps+1))
                        visited.add(nextGene)

        return -1

        