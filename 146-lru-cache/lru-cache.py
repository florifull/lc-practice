class Node:
    def __init__(self, value=None, key=None, prev=None, nxt=None):
        self.value, self.key = value, key
        self.prev, self.next = prev, nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyToNode = {}  # keys to node objects
        self.LRU = Node()  # Head sentinel
        self.MRU = Node()  # Tail sentinel
        self.LRU.next, self.MRU.prev = self.MRU, self.LRU

    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_mru(self, node):
        prev_mru = self.MRU.prev
        prev_mru.next = node
        node.prev = prev_mru
        node.next = self.MRU
        self.MRU.prev = node

    def get(self, key: int) -> int:
        if key in self.keyToNode:
            node = self.keyToNode[key]
            # Move the accessed node to the MRU position.
            self._remove_node(node)
            self._add_to_mru(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keyToNode:
            # If key exists, update value and move to MRU.
            node = self.keyToNode[key]
            node.value = value
            self._remove_node(node)
            self._add_to_mru(node)
        else:
            # If key doesn't exist, create a new node.
            new_node = Node(value, key)
            self.keyToNode[key] = new_node
            self._add_to_mru(new_node)
            
            # Check for capacity and remove LRU if necessary.
            if len(self.keyToNode) > self.capacity:
                # The LRU node is the one right after the LRU sentinel.
                lru_node = self.LRU.next
                self._remove_node(lru_node)
                del self.keyToNode[lru_node.key]