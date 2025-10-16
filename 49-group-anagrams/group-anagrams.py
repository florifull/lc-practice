class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        uni_to_strings = collections.defaultdict(list)
        # T: O(m * n)
        for word in strs:
            uni = [0] * 26
            for c in word:
                uni[ord(c) - ord('a')] += 1
            uni_to_strings[tuple(uni)].append(word) # {(101...0):['helloo']}
        return list(uni_to_strings.values())