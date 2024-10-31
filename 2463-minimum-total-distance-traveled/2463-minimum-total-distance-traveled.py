class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort(); factory.sort()
        rlen, flen = len(robot), len(factory)
        
        @lru_cache(None)
        def knapsack(i, j, cap):
            if i==rlen: 
                return 0
            
            if cap==0: 
                if j+1 < flen:
                    return knapsack(i, j+1, factory[j+1][1])
                return float("inf")
            
            res = []
            
            res.append(abs(factory[j][0] - robot[i]) + knapsack(i+1, j, cap-1))
            
            if j+1<flen:
                res.append(knapsack(i, j+1, factory[j+1][1]))
            
            return min(res)
        
        return knapsack(0, 0, factory[0][1])