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
        # for i in range(len(word)):
        #     new_w = word[:i] + word[i+1:]
        #     new_w_map = collections.Counter(new_w)
        #     if max(new_w_map.values()) == min(new_w_map.values()): return True
        # return False
    # T: O(n^2), S: O(n)