class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        cache = {}
        robot.sort(); factory.sort()
        rlen, flen = len(robot), len(factory)
        
        def knapsack(i, j, cap):
            key = (i, j, cap) 
            if key in cache: return cache[key]
            
            if i==rlen: 
                cache[key] = 0
                return cache[key]
            
            if cap==0: 
                if j+1 < flen:
                    cache[key] = knapsack(i, j+1, factory[j+1][1])
                    return cache[key]
                cache[key] = float("inf")
                return cache[key]
            
            res = []
            
            res.append(abs(factory[j][0] - robot[i]) + knapsack(i+1, j, cap-1))
            
            if j+1<flen:
                res.append(knapsack(i, j+1, factory[j+1][1]))
            
            cache[key] = min(res)
            return cache[key]
        
        return knapsack(0, 0, factory[0][1])