class Node:
    def __init__(self, terminal=False):
        self.isTerminal = terminal
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word[:-1]:
            if c not in curr.children:
                newNode = Node()
                curr.children[c] = newNode  
            curr = curr.children[c]
        if word[-1] not in curr.children:
            newNode = Node(True)
            curr.children[word[-1]] = newNode
        curr.children[word[-1]].isTerminal = True

    def search(self, word: str) -> bool:
        curr = self.root
        def dfs(node, word):
            if not node: return False
            if not word: return node.isTerminal
            c1, crest = word[0], word[1:]
            if c1 == '.':
                for _, node in node.children.items():
                    if dfs(node, crest): return True
                return False
            else:
                if c1 not in node.children:
                    return False
                return dfs(node.children[c1], crest)
            return False
        return dfs(curr, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)