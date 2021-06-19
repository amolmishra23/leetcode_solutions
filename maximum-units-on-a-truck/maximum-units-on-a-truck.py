class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        res = 0
        
        for i in range(len(boxTypes)):
            temp = truckSize
            truckSize -= boxTypes[i][0]
            res += min(temp, boxTypes[i][0])*boxTypes[i][1]
            if truckSize<=0: return res
            
        return res
        