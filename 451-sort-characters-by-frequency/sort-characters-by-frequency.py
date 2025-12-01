class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)  # char -> freq
        buckets = defaultdict(list)  # freq -> [char]

        for char, freq in count.items():
            buckets[freq].append(char)

        res = []
        for i in range(len(s), 0, -1):
            if i in buckets:
                for c in buckets[i]:
                    res.append(c * i)

        return "".join(res)