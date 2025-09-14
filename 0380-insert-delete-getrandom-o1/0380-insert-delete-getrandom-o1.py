import random
class RandomizedSet:

    def __init__(self):
        self.num = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.num)
        self.num.append(val)
        
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        idx = self.pos[val]
        last_val = self.num[-1]

        self.num[idx] = last_val
        self.pos[last_val] = idx

        self.num.pop()

        del self.pos[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.num)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()