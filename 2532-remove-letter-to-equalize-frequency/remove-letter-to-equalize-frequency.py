class Solution:
    def equalFrequency(self, word: str) -> bool:
        ourMap = collections.Counter(word)
        found = False
        for c in list(ourMap.keys()):
            ourMap[c] -= 1
            if ourMap[c] == 0:
                del ourMap[c]
            if max(ourMap.values()) == min(ourMap.values()): found = True
            ourMap[c] = ourMap.get(c, 0) + 1
        return found
    # T: O(n), S: O(26)