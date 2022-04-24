class UndergroundSystem:

    def __init__(self):
        self.check_in = {}
        self.route_time, self.route_count = defaultdict(int), defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        check_in = self.check_in.pop(id)
        
        self.route_time[(check_in[0], stationName)] += t-check_in[1]
        self.route_count[(check_in[0], stationName)] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        return self.route_time[route]/self.route_count[route]
        

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)