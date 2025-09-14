"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        oldToNew = {}

        def dfs(n):
            # if our old node already mapped to a new node..
            if n in oldToNew: return oldToNew[n]
            oldToNew[n] = Node(n.val)
            newNode = oldToNew[n]
            for nei in n.neighbors:
                newNode.neighbors.append(dfs(nei))
            return newNode
        return dfs(node)
    # T: O(v + e), S: O(v + 3)