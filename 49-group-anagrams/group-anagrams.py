class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        occs_to_words = collections.defaultdict(list)
        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c) - ord('a')] += 1
            occs_to_words[tuple(chars)].append(s)
        return [v for v in occs_to_words.values()]
    # T: O(n * s), S: O(n)