
from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radient = deque()
        dire = deque()
        n = len(senate)

        for i, ch in enumerate(senate):
            if ch == "R":
                radient.append(i)
            else:
                dire.append(i)
        
        while radient and dire:
            r_i = radient.popleft()
            d_i = dire.popleft()
            if r_i < d_i:
                radient.append(r_i+n)
            else:
                dire.append(d_i+n)
        return "Radiant" if radient else "Dire"
