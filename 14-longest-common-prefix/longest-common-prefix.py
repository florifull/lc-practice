class Node:
    def __init__(self):
        self.children = {}
        self.isTerminal = False

class Solution:
    def __init__(self):
        self.root = Node()
    
    def add(self, s):
        curr = self.root
        for c in s:
            if c not in curr.children:
                newChild = Node()
                curr.children[c] = newChild
            curr = curr.children[c]
        curr.isTerminal = True

    def startsWith(self, s):
        # if we get to a terminal node OR a node with more than 1 child - BREAK
        # (no longer global common prefix..)
        curr = self.root
        prefix = []
        for c in s:
            if len(curr.children) > 1 or curr.isTerminal:
                return ''.join(prefix)
            prefix.append(c)
            curr = curr.children[c]
        return ''.join(prefix)

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return None
        if len(strs) == 1: return strs[0]
        # add all strings to trie
        for s in strs:
            self.add(s)
        return self.startsWith(strs[0])