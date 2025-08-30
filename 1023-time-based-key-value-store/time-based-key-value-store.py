class TimeMap:

    def __init__(self):
        # store values in a hashmap -> key s : val [(val, timestamp)]
        # ourMap ex: {foo : [(bar, 1), (bar2, 4)]}
        self.ourMap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ourMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        ourList = self.ourMap[key]
        l, r = 0, len(ourList) - 1
        largestTimestampStringPair = [-1, '']
        while l <= r:
            m = (l + r) // 2
            middleTimeStamp = ourList[m][1]
            ourString = ourList[m][0]
            if middleTimeStamp == timestamp: return ourString
            # binary search
            if middleTimeStamp < timestamp:
                largestTimestampStringPair = [middleTimeStamp, ourString]
                l = m + 1
            else: 
                # middleTimeStamp is greater than timestamp
                r = m - 1
        return largestTimestampStringPair[1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)