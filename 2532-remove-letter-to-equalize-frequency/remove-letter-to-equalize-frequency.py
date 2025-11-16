class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            new_w = word[:i] + word[i+1:]
            new_w_map = collections.Counter(new_w)
            if max(new_w_map.values()) == min(new_w_map.values()): return True
        return False
    # T: O(n^2), S: O(n)