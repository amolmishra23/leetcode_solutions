class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        No need to worry about cities in between, and recount from there. Even they will fail mostly.
        As from i,i+1...j. If at j we were out of fuel, definitely will be out of fuel at i+1 also. 
        
        Because we are guaranteed to have an answer, hence start everytime from very next index.
        Wherever we stopped, because of fuel insufficiency. 
        """
        
        if len(gas)==0 or len(cost)==0 or sum(gas)<sum(cost): return -1
        
        pos, bal = 0, 0
        
        for i in range(len(gas)):
            bal += (gas[i]-cost[i])
            if bal<0:
                bal = 0
                pos = i+1
                
        return pos