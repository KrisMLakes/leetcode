from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
       # wins = defaultdict(int)
        loses= defaultdict(int)
        players = defaultdict(int)
        #arr1 = []
        for winner, loser in matches:
           # wins[winner] = wins[winner] + 1
            loses[loser] = loses[loser] + 1
            players[winner] = players[winner] + 1
            players[loser] = players[loser] + 1
            
        no_loss = [player for player in players if loses[player]==0]
        one_loss = [player for player in players if loses[player]==1]
        
        return [sorted(no_loss), sorted(one_loss)]
            
            
            
        #for i in range(len(loses)):
            #if loses[i]==1:
            #    arr1.append(i)
        #output=List[List[int]]     
       # print (wins)
        #print (loses)
        #output.append(wins.keys() not in loses.keys())
        #output.append(arr1)
        