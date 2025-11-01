class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return None
        prefix = strs[0]
        for pre in strs[1:]:
            while not pre.startswith(prefix):
                prefix = prefix[:-1]
        return prefix
    # T: O(m * n), S: O(1)