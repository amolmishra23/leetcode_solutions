class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: -x[1])
        res = 0
        
        for box, units in boxTypes:
            if truckSize>box:
                res += (box*units)
                truckSize -= box
            else:
                res += (truckSize*units)
                return res
        
        return res