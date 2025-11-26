class OrderedStream:

    def __init__(self, n: int):
        self.storage = [0] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.storage[idKey-1] = value
        if self.ptr == idKey-1:
            res = []
            i = self.ptr
            while i < len(self.storage) and self.storage[i]:
                res.append(self.storage[i])
                i += 1
            self.ptr = i
            return res
        return []

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)