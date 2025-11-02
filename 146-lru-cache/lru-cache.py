class Node():
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {} #key:num , value:node object
        self.capacity = capacity
        # left = LRU, right = MRU
        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        # remove node (passed in LRU node)
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev


    def insert(self, node):
        # insert at right
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # make this node the MRU
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        newNode = Node(key, value)
        self.cache[key] = newNode
        self.insert(newNode)
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)