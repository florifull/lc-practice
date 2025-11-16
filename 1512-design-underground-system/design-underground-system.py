class UndergroundSystem:
# trips => (startstation, endstation) = (id, numtrips, totalTime)
    def __init__(self):
        self.idToStart = {} # id: (startStation, time)
        self.StartEndTotal = {} # (startStation, endStation):[totalTime, totalTrips]
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # id to check in stationName, time
        self.idToStart[id] = (stationName, t)
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # startStation,Endstation to total Time
        # retrieve start from id
        startStation, checkInTime = self.idToStart[id]
        timediff = t - checkInTime
        if (startStation,stationName) not in self.StartEndTotal:
            self.StartEndTotal[(startStation,stationName)] = [0, 0]
        # increment total trips and total time difference
        self.StartEndTotal[(startStation,stationName)][0] += timediff
        self.StartEndTotal[(startStation,stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTimeDiff = self.StartEndTotal[(startStation,endStation)][0]
        totalTrips = self.StartEndTotal[(startStation,endStation)][1]
        return totalTimeDiff / totalTrips

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)