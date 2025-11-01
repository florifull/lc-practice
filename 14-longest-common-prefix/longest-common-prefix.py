class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return None
        prefix = strs[0]
        for pre in strs[1:]:
            while not pre.startswith(prefix):
                prefix = prefix[:-1]
        return prefix
    # T: O(s), S: O(1) - where s is the sum of all characters