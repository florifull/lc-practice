class RandomizedSet:

    def __init__(self):
        self.map = {} # val to index held in self.items
        self.items = [] # for getting random access (holds actual vals)

    def insert(self, val: int) -> bool:
        if val in self.map: return False
        insert_idx = len(self.items)
        self.map[val] = insert_idx
        self.items.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map: return False
        occ_idx = self.map[val]
        # since removing is O(n), we can pop in O(1), so replace last ele with target
        self.items[occ_idx], self.items[-1] = self.items[-1], self.items[occ_idx]
        replaced_val = self.items[occ_idx]
        self.map[replaced_val] = occ_idx
        remove_val = self.items.pop()
        del self.map[remove_val]
        return True

    def getRandom(self) -> int:
        randomIdx = random.randint(0, len(self.items)-1)
        return self.items[randomIdx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()