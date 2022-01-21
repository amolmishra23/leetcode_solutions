class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas)==0 or len(cost)==0 or sum(gas)<sum(cost): return -1
        
        pos, bal = 0, 0
        
        for i in range(len(gas)):
            bal += (gas[i]-cost[i])
            if bal<0:
                bal = 0
                pos = i+1
                
        return pos